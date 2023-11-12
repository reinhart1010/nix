---
layout: page
title: common/7zr (中文)
description: "一个高压缩率的文件归档器。"
content_hash: ea0d5e378b74719ca15674697ec683fac5dddfc7
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/7zr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7zr.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7zr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7zr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# 7zr

一个高压缩率的文件归档器。
类似于 `7z`，只支持 `.7z` 文件。
更多信息：<https://manned.org/7zr>.

- 归档一个文件或目录：

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录</span>

- 加密一个已存在的归档文件（包括文件名）：

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">加密文件.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件.7z</span>

- 提取一个已存在的 7z 文件，并保持原来的目录结构：

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件.7z</span>

- 提取一个归档文件到指定的输出目录：

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出目录</span>

- 提取一个归档文件到标准输出：

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件.7z</span>` -so`

- 列出一个归档文件的内容：

`7zr l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">归档文件.7z</span>

- 列出可用的归档文件类型：

`7zr i`
