---
layout: page
title: common/autossh (English)
description: "Run, monitor and restart SSH connections."
content_hash: a4a8c9458fc82adb2b83cd2339d908b22af8737f
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/autossh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autossh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autossh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/autossh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/autossh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autossh

Run, monitor and restart SSH connections.
Auto-reconnects to keep port forwarding tunnels up. Accepts all `ssh` flags.
More information: <https://www.harding.motd.ca/autossh>.

- Start an SSH session, restarting when a monitoring port fails to return data:

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_port</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_command</span>`"`

- Forward a local port to a remote one, restarting when necessary:

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_port</span>` -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Fork `autossh` into the background before executing `ssh` and don't open a remote shell:

`autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_port</span>` -N "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_command</span>`"`

- Run in the background, with no monitoring port, and instead send SSH keep-alive packets every 10 seconds to detect failure:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_command</span>`"`

- Run in the background, with no monitoring port and no remote shell, exiting if the port forward fails:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Run in the background, logging `autossh` debug output and `ssh` verbose output to files:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/autossh_log_file.log</span>` autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">monitor_port</span>` -v -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/ssh_log_file.log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_command</span>
