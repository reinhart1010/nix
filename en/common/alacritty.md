---
layout: page
title: common/alacritty (English)
description: "Cross-platform, GPU-accelerated terminal emulator."
content_hash: f6c217999b3e9d169f9e8699f044d6c3254919f5
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
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
  - title: português (Brasil) version
    url: /pt_BR/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
---
# alacritty

Cross-platform, GPU-accelerated terminal emulator.
More information: <https://github.com/alacritty/alacritty>.

- Open a new Alacritty window:

`alacritty`

- Run in a specific directory:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Run a command in a new Alacritty window:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Specify alternative configuration file (defaults to `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yml</span>

- Run with live config reload enabled (can also be enabled by default in `alacritty.yml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yml</span>
