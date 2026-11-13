---
name: cloud-desktop
description: Use in a managed Codex Cloud chat to open a URL in shared Chrome, inspect a Linux app, show the Desktop panel, or diagnose missing computer-use tools.
---

# Use the shared cloud desktop

When the chat’s environment context identifies a managed cloud executor, use
its Chrome for “open this URL” or “check in the browser” unless the user
names another browser or device.

Chrome and native apps share one Linux display (X11). Codex can use the
computer-use tools with the Desktop panel closed. Opening the panel lets the
user watch and take control of the same screen. Closing it disconnects the
viewer and leaves the desktop running.

## What starts on demand

On an on-demand desktop, Codex can discover the tools and check status while
the display stays asleep. The first valid desktop `js` call starts the display
before running the code. Connecting the Desktop viewer also starts it.
Chrome has its own startup setting. When configured to start closed, it
launches on the first browser operation that needs it, such as opening a tab.

## Open and inspect

Look for the desktop JavaScript tool (usually `cua_repl.js`) among the tools
offered directly to this turn. Follow its first-call instructions. For a new
tab in Chrome, `await cua.createBrowserTab("cdp", url)` can be the first
action when offered, even with the panel closed.
Use `await cua.getState()` to discover available browsers and apps. For an
existing tab, follow the runtime’s tab-selection or claiming instructions.
Inspect the page before reporting what loaded. Use Sky for native windows
or a full-screen screenshot when available.

## Show the user

When the user asks to watch or needs to act, such as completing sign-in, call
`open_in_codex({"target":{"type":"cloud-desktop"}})` if offered. In supported
Codex desktop chats, the user can also open the right side panel and choose
**New tab (+) → Desktop**. Let the user **Take over** and select **Return
control** when finished. Pause agent input during the handoff, then inspect
the same page before continuing.

## If control is unavailable

Call `cloud_environment.environment_status({})` and match its `environment_id`
to the selected executor. Check `capabilities[].remote_desktop`. A cold desktop
can report `enabled: true` with `state: unknown`. If the environment is
starting, recheck the tools once it is ready. Report the environment ID,
desktop status, and which tool was missing or which call failed. Say what
you could verify. If only the viewer works, offer to open it for the user.
