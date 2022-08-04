---
layout: page
title: common/brew (中文)
description: "Linux 和 macOS 的包管理器。"
content_hash: a58736a673124792e4be870cc1c0b17d960b12fe
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
---
# brew

Linux 和 macOS 的包管理器。
更多信息：<https://brew.sh>.

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

- 檢查本地 Homebrew 安裝包是否有潛在問題：

`brew doctor`
