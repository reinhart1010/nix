---
layout: page
title: common/frpc (English)
description: "Connect to a `frps` server to start proxying connections on the current host."
content_hash: 7aceac88c18b4e04dab5e6fd3c31dd72bcf881e9
last_modified_at: 2024-06-16
tldri18n_status: 2
---
# frpc

Connect to a `frps` server to start proxying connections on the current host.
Part of `frp`.
More information: <https://github.com/fatedier/frp>.

- Start the service, using the default configuration file (assumed to be `frps.ini` in the current directory):

`frpc`

- Start the service, using the newer TOML configuration file (`frps.toml` instead of `frps.ini`) in the current directory:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Start the service, using a specific configuration file:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if the configuration file is valid:

`frpc verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print autocompletion setup script for Bash, fish, PowerShell, or Zsh:

`frpc completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Display version:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
