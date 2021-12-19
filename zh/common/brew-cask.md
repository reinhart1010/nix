---
layout: page
title: common/brew-cask (中文)
description: "macOS 上的应用程序包管理工具。"
content_hash: 0456830b08765d249e87a7ae1474f7ec478f0850
related_topics:
  - title: Deutsch version
    url: /de/common/brew-cask.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/brew-cask.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-cask.html
    icon: bi bi-globe
---
# brew cask

macOS 上的应用程序包管理工具。
更多信息：<https://github.com/Homebrew/homebrew-cask>.

- 模糊搜索可用命令行工具和软件包：

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件名</span>

- 安装一个软件：

`brew cask install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件名</span>

- 列出全部已安装软件：

`brew cask list`

- 列出全部已安装的软件中，可以升级的：

`brew cask outdated`

- 将一个已安装的软件升级到最新的版本：

`brew cask upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件名</span>

- 删除一个软件（仅通过 brew cask install 方式安装的）：

`brew cask uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件名</span>

- 卸载一个软件并删除相关的设置和文件：

`brew cask zap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件名</span>

- 显示指定软件的相关信息：

`brew cask info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件名</span>
