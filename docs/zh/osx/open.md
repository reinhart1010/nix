---
layout: page
title: osx/open (中文)
description: "打开文件、目录和应用程序。"
content_hash: c1f0c4dbc295d6af3b806451505472220dd65e97
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/open.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/open.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/open.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/open.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># open

打开文件、目录和应用程序。
更多信息：<https://keith.github.io/xcode-man-pages/open.1.html>.

- 使用系统关联的应用程序打开文件：

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.extension</span>

- 运行图形化的 macOS 应用程序：

`open -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用程序名</span>

- 运行指定 包名 的图形化 macOS 应用程序（请参阅`OSascript`命令，查询如何获取应用程序的 包名）：

`open -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.domain.application 应用程序包名</span>

- 在"访达（finder）"中打开当前文件夹：

`open .`

- 打开"访达（finder）", 并且给出指定文件：

`open -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>

- 使用系统默认应用程序，打开当前目录中所有给定扩展名的文件：

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.extension</span>
