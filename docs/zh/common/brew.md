---
layout: page
title: common/brew (中文)
description: "Linux 和 macOS 的包管理器。"
content_hash: 408a962c0b4f9bcdbbf6f5d424fb86b1016bba39
last_modified_at: 2023-11-06
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
---
# brew

Linux 和 macOS 的包管理器。
更多信息：<https://docs.brew.sh/Manpage>.

- 安装最新稳定版的配方（formula）或木桶（cask），使用 `--devel` 安装开发版：

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配方</span>

- 列出所有已安装的配方和木桶：

`brew list`

- 升级已安装的配方或木桶（如果没有指定，则升级所有已安装的配方/木桶）：

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配方</span>

- 从 Homebrew 源存储库中获取最新版本的 Homebrew 以及所有配方和木桶：

`brew update`

- 显示有新版本的配方和木桶：

`brew outdated`

- 搜索可用的配方（即包）和木桶（即原生包）：

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 显示有关配方或木桶的信息（版本、安装路径、依赖等）：

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配方</span>

- 检查本地 Homebrew 安装包是否有潜在问题：

`brew doctor`
