---
layout: page
title: common/alacritty (English)
description: "Cross-platform, GPU-accelerated terminal emulator."
content_hash: 92889d40e0c528a44a91bdd04829aa76b91c89e8
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alacritty.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alacritty.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alacritty.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alacritty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alacritty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alacritty.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alacritty.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alacritty

Cross-platform, GPU-accelerated terminal emulator.
More information: <https://github.com/alacritty/alacritty>.

- Start a new Alacritty process and create a window:

`alacritty`

- Start the Alacritty daemon (without creating a window):

`alacritty --daemon`

- Create a new window using the already running Alacritty process:

`alacritty msg create-window`

- Start the shell in a specific directory (also works with `alacritty msg create-window`):

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- [e]xecute a command in a new Alacritty window (also works with `alacritty msg create-window`):

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Use an alternative configuration file (defaults to `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>

- Run with live configuration reload enabled (can also be enabled by default in `alacritty.toml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.toml</span>
