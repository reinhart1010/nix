---
layout: page
title: common/frps (English)
description: "Quickly set up a reverse proxy service."
content_hash: 4284ad56f90b2abd309f7ae4096102ea23fa6173
last_modified_at: 2024-06-16
tldri18n_status: 2
---
# frps

Quickly set up a reverse proxy service.
Part of `frp`.
More information: <https://github.com/fatedier/frp>.

- Start the service, using the default configuration file (assumed to be `frps.ini` in the current directory):

`frps`

- Start the service, using the newer TOML configuration file (`frps.toml` instead of `frps.ini`) in the current directory:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Start the service, using a specified config file:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Check if the configuration file is valid:

`frps verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Print autocompletion setup script for Bash, fish, PowerShell, or Zsh:

`frps completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Display version:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
