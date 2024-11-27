---
layout: page
title: common/brew (中文)
description: "Homebrew - 一个 macOS 和 Linux 的包管理器。"
content_hash: adc780ec44082842e19d196e5b1148e1c5543c0a
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew

Homebrew - 一个 macOS 和 Linux 的包管理器。
此命令也有关于其子命令的文件，例如：`install`.
更多信息：<https://docs.brew.sh/Manpage>.

- 安装最新稳定版本的软件包或安装包（使用 `--devel` 安装开发版本）：

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 列出所有已安装的软件包和安装包：

`brew list`

- 升级已安装的软件包或安装包（如果未指定，则升级所有已安装的软件包或安装包）：

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 从 Homebrew 源代码仓库中获取 Homebrew 和所有软件包及安装包的最新版本：

`brew update`

- 显示有更新版本可用的软件包和安装包：

`brew outdated`

- 搜索可用的软件包（即包）和安装包（即本地 macOS `.app` 包）：

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包名称</span>

- 显示有关软件包或安装包的信息（版本、安装路径、依赖项等）：

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 检查本地的 Homebrew 安装中的潜在问题：

`brew doctor`
