---
layout: page
title: osx/softwareupdate (中文)
description: "通过命令行更新 macOS 应用商店中应用程序的工具。"
content_hash: 650c709790eabb7483dba183e1ea251efd412b7f
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/softwareupdate.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/softwareupdate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# softwareupdate

通过命令行更新 macOS 应用商店中应用程序的工具。
更多信息：<https://keith.github.io/xcode-man-pages/softwareupdate.8.html>.

- 列出所有可用的更新：

`softwareupdate --list`

- 下载并安装所有更新：

`softwareupdate --install --all`

- 下载并安装所有推荐的更新：

`softwareupdate --install --req`

- 下载并安装特定的应用程序：

`softwareupdate --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">更新应用程序名</span>
