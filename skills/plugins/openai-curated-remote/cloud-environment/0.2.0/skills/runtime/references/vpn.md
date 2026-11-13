# Tailscale VPN access

Use this reference when the local policy reports `vpn_configured: true` or when
explicitly diagnosing VPN or private-network access, even if the flag is missing
or false. Read [Cloud environment networking](networking.md) for HTTP policy and
proxy setup. `environment_status` reports configured VPN capabilities and observed
enrollment failures. A null `capabilities[].vpn.failure` means no current failure
is reported; it does not establish VPN readiness. Check connectivity with a request
to the required service as described below.

## Choose the connection path

Tailscale runs in the sidecar. The executor has no VPN interface or general
Internet route. Direct connections, route changes, or unsetting proxy variables
cannot enable VPN access. Sidecar controls and VPN credentials are unavailable
from the executor. When offered, `environment_diagnostics` provides retained
capture metadata and, with explicit repair consent, selected redacted logs.
Follow the runtime skill's diagnostic flow; do not install or reconfigure
Tailscale in the executor to repair access.

| Use | Endpoint | Policy and authentication |
| --- | --- | --- |
| HTTP/HTTPS | Inherited `HTTP_PROXY`/`HTTPS_PROXY` in the default agent sandbox | With automatic Tailscale access, tailnet destinations need no public-internet grant. Keep this path for injected credentials. |
| Raw TCP | HTTP CONNECT at `proxy:8088` from the outer executor | VPN access; older environments also require a TCP grant. Opaque bytes, no TLS interception or credential injection. The application supplies authentication; proxy credential placeholders will not work. |

When `/etc/codex/network-policy.json` reports `automatic_tailscale_access: true`,
the sidecar authorizes Tailscale destinations without manual domain or CIDR grants.
Public internet means non-Tailscale transport, including when a tailnet advertises
a publicly numbered subnet. Public HTTP policy still governs direct connections;
raw TCP remains Tailscale-only. Protected platform destinations remain blocked.
If the field is absent or false, use the legacy grant rules below.

## Access and recovery

1. Inspect the selected executor's policy snapshot and current environment status.
   If VPN configuration is missing or false, report that setup gap; do not treat
   it as a working VPN or change the snapshot to enable access.
2. For HTTP/HTTPS, make a bounded request to the actual authorized service using
   the inherited proxy settings, for example `curl -i --max-time 20 <service-url>`.
   Keep TLS verification enabled. A successful request to another host does not
   prove that this service or its Tailnet hostname is reachable.
3. If an otherwise authorized request fails with a sandbox or proxy-connectivity
   error, retry the same bounded request using the execution tool's normal
   approval flow (`sandbox_permissions: "require_escalated"` where supported).
   Preserve the inherited proxy settings and CA trust. Do not unset proxy
   variables or use `--noproxy` for the remote VPN destination. If escalation is
   unavailable or denied, report the limitation. An explicit destination-policy
   denial requires the appropriate policy change, not an escalation retry.
4. Compare the status and sanitized error from each attempt. If an integrated
   terminal request succeeds while an agent request fails, or only the escalated
   request succeeds, that indicates different execution paths. Do not infer
   an account or rollout problem from "proxy unreachable" alone.
5. If access still fails, distinguish DNS resolution, policy rejection, sidecar
   readiness, and service/protocol errors using the guidance below. Report the
   destination, port, execution path, and sanitized error. Inspect retained
   diagnostic metadata even when the failing layer is outside the executor;
   after repair consent, select a relevant capture to read. If evidence is
   unavailable or insufficient, escalate the environment and capture IDs and
   the unresolved question without copying credentials.

For raw TCP, use the authorized forwarding workflow below. A protected-destination
denial must not be worked around by switching listeners.

Saved VPN configuration is separate from running enrollment. **Save draft** does
not reconnect or re-enroll the current VPN. A newly added VPN needs **Publish**;
a changed key needs fresh VPN enrollment before the running environment uses it.
Follow the existing configuration review and approval flow, then validate access
to the intended service. Do not infer applied enrollment from a displayed saved
configuration or from an older diagnostic capture.

## DNS and service identity

Fresh VPN proxy enrollment accepts the tailnet's DNS settings, including split
DNS and MagicDNS, for HTTP/HTTPS and CONNECT hostname resolution. Proxies enrolled
before this support was deployed need recreation and fresh enrollment; a new chat
or updated skill alone does not update a running proxy's DNS configuration.

Use the service's hostname. Legacy environments also require a matching HTTP or
TCP grant. Executor DNS failure
alone does not disprove hostname CONNECT; preserve the hostname for sidecar
resolution (for example, `resolve=0` with socat).

If a Tailnet hostname fails while its known, authorized IP works, diagnose DNS
separately. Use the IP only where the protocol and destination policy permit it;
in legacy environments, a raw TCP literal IPv4 needs a matching CIDR grant. Preserve the service's
TLS hostname/SNI and certificate verification when changing the transport
address, as in the forwarding examples below. Do not disable verification to
make an IP-based HTTPS request succeed.

## Legacy TCP grants

TCP grants apply only to 8088; HTTP rules do not authorize that listener.
A literal IPv4 address needs a matching CIDR. A hostname needs an exact
domain or `*.` wildcard match; wildcards exclude the apex. Domain grants need no
additional CIDR grant. Current grants cover all TCP ports. Resolved IPv4 addresses
must select Tailscale transport; platform-protected
destinations remain blocked. Changed TCP grants require a replacement environment
using the new configuration version.

## Install the forwarding tool at runtime

Use the bundled [socat installer](../scripts/ensure-socat.sh) before creating a
forward. Set `RUNTIME_SKILL_DIR` to the absolute directory containing this skill's
`SKILL.md`, then capture the executable path it prints:

```sh
SOCAT="$(bash "$RUNTIME_SKILL_DIR/scripts/ensure-socat.sh")"
```

If the skill is available only through resource reads, read the linked installer,
save it in the selected executor, and invoke `bash` on that saved path instead.

The installer downloads pinned, checksum-verified socat and libwrap packages into
`${XDG_CACHE_HOME:-$HOME/.cache}/cloud-environment`. It needs no root access or
system package changes, and reuses the cached runtime without downloading again.
The patched socat version is independent of the executor image's APT snapshot.

This runtime supports Linux x86_64 with glibc 2.38 or newer and OpenSSL 3
(`libssl.so.3` and `libcrypto.so.3`), including `cloud-agent-base`. Installation
requires `bash`, `curl`, `sha256sum`, and `dpkg-deb`. Other images may use their
own maintained socat installation; set `SOCAT` to that executable's absolute path.

First-time downloads use the inherited HTTP proxy and require permitted HTTPS
access to `deb.debian.org`. A TCP grant does not authorize these downloads. If
HTTP policy denies them, explicitly suggest temporarily adding the exact host
`deb.debian.org` through the reviewed HTTP configuration flow for HTTPS downloads.
Preserve existing rules and wait for the updated policy to be enforced in the
selected environment. After installation succeeds and rerunning the installer
confirms cache reuse, suggest removing only the rule added for this installation
through the same flow. A replacement environment or cleared cache may need
download access again. An existing maintained socat is also an option. Do not
bypass the proxy or disable TLS verification.

## Forward an authorized endpoint

For an agent-issued TCP forward, request `sandbox_permissions: "require_escalated"`
for the command that connects to `proxy:8088`. Run the forward and its client
in the same outer network namespace, for example in the same approved command.
A separate default sandbox command has its own loopback and cannot use the
outer listener. If escalation is unavailable or denied, report that limitation.

```sh
"$SOCAT" -d -d TCP4-LISTEN:15432,bind=127.0.0.1,reuseaddr,fork \
  PROXY:proxy:db.example.internal:5432,proxyport=8088,resolve=0
```

Choose a free unprivileged loopback port. Keep the process running while the
client runs; retain its execution session or PID/stderr log and stop it afterward.
`resolve=0` preserves the hostname for sidecar authorization and DNS. No custom
proxy header is needed; standard socat lacks `proxy-header`. A listening port
alone proves nothing: CONNECT starts when the application connects.

Preserve TLS server identity and verification while connecting through loopback:

```sh
psql 'host=db.example.internal hostaddr=127.0.0.1 port=15432 sslmode=verify-full'
```

For HTTPS with remote port 443 forwarded to local 18443:

```sh
curl --noproxy '*' \
  --connect-to service.example.internal:443:127.0.0.1:18443 \
  https://service.example.internal/
```

The original URL preserves Host/SNI/certificate identity. This `--noproxy`
exception applies only to a client connecting through an explicitly established
loopback forward; the forward still uses the authorized sidecar CONNECT path.
Do not use it for a direct request to a remote VPN address. Use normal client
configuration for private service CAs; the HTTP interception CA is not the
service CA. Never disable TLS or SSH host-key verification.

## Limits and diagnosis

- TCP only: no UDP, QUIC, ICMP, inbound connections, transparent routing, or
  automatic cluster discovery. Additional endpoints need authorization and forwards.
- Shell/enterprise restrictions can independently block listeners or `proxy:8088`;
  request access through that policy's supported workflow.
- Check `"$SOCAT" -V`, `getent hosts proxy`, and `ss -ltn`. Rerun the installer
  to recover the cached executable path. If a previously working cache is damaged,
  remove only its versioned socat directory and rerun the installer.
- Make a real client connection. A proxy 403 means an invalid CONNECT request
  or rejected policy/destination;
  `vpn_no_ipv4` means no IPv4 answer; `vpn_protected_destination` rejects protected
  or nonprivate addresses. If no grant matches, request a reviewed configuration change.
  503 `vpn_not_ready` or `vpn_policy_unavailable` needs operator
  investigation. Report destination, port, and sanitized status/stderr.
- Successful CONNECT proves only TCP transport. Then check protocol, TLS/CA,
  and application authentication. Timeouts can involve VPN ACLs, subnet-route
  approval, firewalls, or service listeners; ask the operator for sidecar diagnostics.
  Recreate forwards after environment restart; reconnect clients after VPN loss.
