# Cloud environment networking

## Network proxy

> **Network requests go through an isolated proxy sidecar.**

Use the supplied `HTTP_PROXY`, `HTTPS_PROXY`, and CA trust settings with TLS
verification enabled. The proxy routes outbound HTTP/HTTPS traffic, checks
destinations, and applies configured credentials to matching HTTPS requests.
HTTPS usually uses TLS inspection with the supplied CA; configured passthrough
routes preserve end-to-end TLS. Check route compatibility for clients with
certificate pinning or custom trust stores.

The default agent command runs inside bubblewrap. Its inherited proxy variables
can point to a loopback bridge that forwards to the managed proxy. In either
HTTP policy mode, keep the values supplied to the command, including lowercase
variants and `NO_PROXY`. To test access, run `curl --max-time 20 "$service_url"`
with the actual destination URL. If a client requires an explicit proxy setting,
use the inherited value for that protocol.

The sidecar addresses in the policy snapshot are for the outer executor. Only
an approved agent command running outside bubblewrap can dial them directly.
If a sandboxed probe resolves `proxy` but reports “Network is unreachable” for
`proxy:8080`, retry the destination with inherited settings before diagnosing
an outage or requesting a policy change. Reserve direct probes for questions
about the sidecar itself. Escalation still leaves Cloud destination policy in force.

The proxy resolves destination hostnames. In restricted environments, local DNS
lookups can fail while proxied HTTP succeeds; diagnose connectivity with the
actual proxied request. Supplied `NO_PROXY` settings keep loopback traffic local.

Outbound rules govern services the environment connects to. Incoming access to
services running in the environment uses the platform's separate preview or
port-forwarding controls.

## Runtime policy

Use these sources to inspect runtime policy:

- `cloud_environment.environment_status`: environment configuration, capabilities, and observed readiness. Refresh after setup or configuration changes.
- `/etc/codex/network-policy.json`: startup policy and proxy settings; this snapshot can be stale.
- `http://proxy:8099/status`: live network policy, VPN settings, and routes. If live status is needed, run this direct probe in the outer executor using an approved escalated command: `curl --noproxy proxy -fsS --max-time 5 http://proxy:8099/status`.

For restricted HTTP access, `network_policy.allowed_hosts` contains custom host
rules, and `presets` lists enabled host bundles. When present,
`preset_allowed_hosts` contains resolved preset rules and `effective_allowed_hosts`
contains the complete desired HTTP allowlist. These fields describe desired
configuration; require `observations_current: true` and
`network_policy.state: enforced` before treating it as applied. The local file's
`http_network_policy.egress_rules` provides the startup expansion.

Exact HTTP host rules cover that hostname across paths, methods, and ports.
`*.example.com` covers subdomains; include `example.com` for the apex. Include
redirect destinations such as download, CDN, and authentication hosts.

Both HTTP modes apply platform destination blocks and protect proxy-local
addresses. Environment registration and initial repository checkout use separate,
scoped platform access rules.

HTTP policy updates apply to subsequent authorization checks while existing
tunnels and streams continue. After a user saves changes during onboarding,
call `cloud_environment.environment_status` again and validate access with a fresh connection.

## Credentials and outbound identities

Use status-reported secret bindings, runtime variable names, and identity aliases
to plan commands. Keep credential values private and use metadata for diagnosis.
Use configured SDKs and CLIs normally: the proxy translates credential placeholders
on matching HTTPS routes. Destination access follows the network policy;
credentials follow each binding's destination and request scope, including
scheme, hostname, port, method, and path.

For CLI or SDK profile selection, read the identity metadata manifest at
`OIC_MANIFEST_PATH` when present. Its version 1 JSON contains a `connections` list.
Select the entry whose `alias` matches the task's intended identity; `is_default`
marks the provider's default. Set these variables for that command from the
selected entry:

| `provider_kind` | Environment variable ← manifest field |
| --- | --- |
| `azure` | `IDENTITY_ENDPOINT` ← `identity_endpoint`; `AZURE_CONFIG_DIR` ← `config_dir` |
| `aws` | `AWS_PROFILE` ← `alias`; `AWS_CONFIG_FILE` ← `config_file` |
| `gcp` | `CLOUDSDK_CONFIG` ← `config_dir`; `CLOUDSDK_ACTIVE_CONFIG_NAME` ← `configuration_name`; `GOOGLE_APPLICATION_CREDENTIALS` ← `credentials_file` |

Preserve inherited authentication headers, guard variables, and injected
credentials. Use credential file paths as selectors. Check the entry's `setup`
outcome when diagnosing CLI failures, and report missing or unsupported manifest
versions, identities, or selector fields.

## Request failures

Inspect the response body and headers to distinguish proxy limits from remote
service errors. The proxy applies rate, size, and duration limits. Honor
`Retry-After` on proxy `429` responses. For `503` responses saying
`Request size too large` or `Average request size too large`, reduce request size
or upload rate respectively. Effective limits depend on the configured route.

## Configured VPN access

Read [Tailscale VPN access](vpn.md) when the local policy reports
`vpn_configured: true` or when explicitly diagnosing VPN or private-network
access, even if the flag is missing or false. It covers the supported HTTP and
TCP routes, connection checks, and troubleshooting. When the local snapshot has
`automatic_tailscale_access: true`, Tailscale destinations need no HTTP or TCP
grant; HTTP policy governs non-Tailscale connections. Older environments use
the separate `tcp_network_access` domain and IP-range grants. Raw TCP always
uses application-supplied authentication.
