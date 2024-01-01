---
layout: page
title: osx/base64 (中文)
description: "使用 Base64 来进行编码和解码。"
content_hash: 50ba65577d1d16b86a3b67130eaf3d60098f0154
last_modified_at: 2024-01-01
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
  - title: italiano version
    url: /it/osx/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/base64.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base64

使用 Base64 来进行编码和解码。
更多信息：<https://www.unix.com/man-page/osx/1/base64/>.

- 编码目标文件：

`base64 --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件</span>

- 解码目标文件：

`base64 --decode --input=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64 编码文件</span>

- 通过标准输入管道进行解码：

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标字符串</span>`" | base64`

- 解码标准输入管道内容：

`echo -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base64 字符串</span>` | base64 --decode`
