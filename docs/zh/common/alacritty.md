---
layout: page
title: common/alacritty (中文)
description: "跨平台，GPU 加速的终端模拟器。"
content_hash: 2d20fdbb554530be4bcdba8010912d1cc9ba9a8d
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alacritty.html
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

- 指定备用配置文件（默认在 `$XDG_CONFIG_HOME/alacritty/alacritty.yml`）：

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/config.yml</span>

- 在启用实时配置重新加载的情况下运行（默认情况下也可以在 `alacritty.yml` 中启用）：

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/config.yml</span>
