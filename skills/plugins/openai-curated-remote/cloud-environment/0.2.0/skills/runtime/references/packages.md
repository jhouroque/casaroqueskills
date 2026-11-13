# Package installation

Keep ordinary development commands, Git, language environments, and builds under
the current user. Use project-local virtual environments and user-owned package
directories for language dependencies.

For system packages, the selected environment may provide a scoped package
installer. If `/usr/local/bin/cloud-agent-packages` is available, use
`sudo -n /usr/local/bin/cloud-agent-packages update` followed by
`sudo -n /usr/local/bin/cloud-agent-packages install <packages>`. Pass exact Debian
package names, optionally with `:architecture` or `=version`. The helper accepts
packages from the environment's approved repositories; it rejects local package
files, repository changes, removals, and extra APT options.

Preserve the inherited proxy settings and CA trust, and keep TLS verification
enabled. Network policy still applies; an explicit destination-policy denial
requires the supported configuration workflow.

If the image already runs as root, invoke the helper directly; the command
sandbox and approval policy still apply.

Sudo cannot elevate inside the command sandbox. Use the execution tool's normal
full command escalation (`sandbox_permissions: "require_escalated"` where
supported), subject to the current approval policy. Additional writable paths
or network access alone do not enable sudo. `environment_status` reports network
and credential readiness, not whether sudo is installed or provisioned.

If escalation is unavailable or denied, or sudo is not provisioned, report that
limitation; do not change sandbox or sudo configuration. After installation,
run tools as the ordinary user. Avoid using sudo for project files, virtual
environments, language package managers, browser, or desktop commands.
