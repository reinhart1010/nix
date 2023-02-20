---
layout: page
title: osx/launchctl (English)
description: "A command-line interface to Apple's `launchd` manager for launch daemons (system-wide services) and launch agents (per-user programs)."
content_hash: 77c0d239a3341533017d32d12c7715c02a6b634a
last_modified_at: 2023-02-20
related_topics:
  - title: 中文 version
    url: /zh/osx/launchctl.html
    icon: bi bi-globe
---
# launchctl

A command-line interface to Apple's `launchd` manager for launch daemons (system-wide services) and launch agents (per-user programs).
`launchd` loads XML-based `*.plist` files placed in the appropriate locations, and runs the corresponding commands according to their defined schedule.
More information: <https://manned.org/launchctl>.

- Activate a user-specific agent to be loaded into `launchd` whenever the user logs in:

`launchctl load ~/Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_script</span>`.plist`

- Activate an agent which requires root privileges to run and/or should be loaded whenever any user logs in (note the absence of `~` in the path):

`sudo launchctl load /Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root_script</span>`.plist`

- Activate a system-wide daemon to be loaded whenever the system boots up (even if no user logs in):

`sudo launchctl load /Library/LaunchDaemons/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system_daemon</span>`.plist`

- Show all loaded agents/daemons, with the PID if the process they specify is currently running, and the exit code returned the last time they ran:

`launchctl list`

- Unload a currently loaded agent, e.g. to make changes (note: the plist file is automatically loaded into `launchd` after a reboot and/or logging in):

`launchctl unload ~/Library/LaunchAgents/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_script</span>`.plist`

- Manually run a known (loaded) agent/daemon, even if it is not the right time (note: this command uses the agent's label, rather than the filename):

`launchctl start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script_file</span>

- Manually kill the process associated with a known agent/daemon, if it is running:

`launchctl stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script_file</span>
