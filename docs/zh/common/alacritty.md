---
layout: page
title: common/alacritty (中文)
description: "跨平台、GPU 加速的终端模拟器。"
content_hash: db5bb2fdd6c51e1e97c74a56afdeceb586a7fff4
last_modified_at: 2025-03-02
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

跨平台、GPU 加速的终端模拟器。
更多信息：<https://github.com/alacritty/alacritty>.

- 启动新的 Alacritty 进程并创建窗口：

`alacritty`

- 启动 Alacritty 守护进程（不创建窗口）：

`alacritty --daemon`

- 使用已运行的 Alacritty 进程创建新窗口：

`alacritty msg create-window`

- 在指定目录启动 shell（也可配合 `alacritty msg create-window` 使用）：

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 执行（[e]xecute）命令到新 Alacritty 窗口（也可配合 `alacritty msg create-window` 使用）：

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 使用替代配置文件（默认使用 `$XDG_CONFIG_HOME/alacritty/alacritty.toml`）：

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/配置.toml</span>

- 启用实时配置重载运行（也可在 `alacritty.toml` 中默认启用）：

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/配置.toml</span>
