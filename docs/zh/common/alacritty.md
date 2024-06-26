---
layout: page
title: common/alacritty (中文)
description: "跨平台，GPU 加速的终端模拟器。"
content_hash: 0b3256452e5d1512e1299eac894c78f5c29178dc
last_modified_at: 2024-05-18
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alacritty.html
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
tldri18n_status: 2
---
# alacritty

跨平台，GPU 加速的终端模拟器。
更多信息：<https://github.com/alacritty/alacritty>.

- 打开一个新的 Alacritty 窗口：

`alacritty`

- 运行在指定目录中：

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径</span>

- 在新的 Alacritty 窗口中运行命令：

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 指定备用配置文件（默认在 `$XDG_CONFIG_HOME/alacritty/alacritty.toml`）：

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/config.toml</span>

- 在启用实时配置重新加载的情况下运行（默认情况下也可以在 `alacritty.toml` 中启用）：

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/config.toml</span>
