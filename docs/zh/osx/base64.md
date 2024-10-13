---
layout: page
title: osx/base64 (中文)
description: "使用 Base64 来进行编码和解码。"
content_hash: 26c94c7318b916f565cc413860c7c825ff39ee00
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/osx/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/base64.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/osx/base64.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/base64.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

使用 Base64 来进行编码和解码。
更多信息：<https://keith.github.io/xcode-man-pages/base64.1.html>.

- 编码目标文件：

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件</span>

- 解码目标文件：

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64 编码文件</span>

- 通过标准输入管道进行解码：

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标字符串</span>`" | base64`

- 解码标准输入管道内容：

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64 字符串</span>` | base64 --decode`
