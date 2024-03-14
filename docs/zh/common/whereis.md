---
layout: page
title: common/whereis (中文)
description: "找到命令的二进制，源文件和手册文件。"
content_hash: 723ad7540f8631e4610e17fedca32455b9e3237d
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/whereis.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/whereis.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># whereis

找到命令的二进制，源文件和手册文件。
更多信息：<https://manned.org/whereis>.

- 找到 SSH 命令的二进制、源文件和手册页：

`whereis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh</span>

- 查找 `ls` 命令的二进制和手册页：

`whereis -bm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- 找到 `gc` 的源文件和 `git` 的手册页：

`whereis -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git</span>

- 仅在 /usr/bin/ 目录中查找 `gcc` 的二进制文件：

`whereis -b -B `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/bin/</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gcc</span>
