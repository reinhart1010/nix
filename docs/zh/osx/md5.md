---
layout: page
title: osx/md5 (中文)
description: "计算 MD5 加密和校验。"
content_hash: b398686ed9b2adef49ea8e6fc6bb5b3f0f0cb476
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/osx/md5.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/md5.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/md5.html
    icon: bi bi-globe
tldri18n_status: 2
---
# md5

计算 MD5 加密和校验。
更多信息：<https://keith.github.io/xcode-man-pages/md5.1.html>.

- 计算一个文件的 MD5 校验值：

`md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 计算多个文件的 MD5 校验值：

`md5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>

- 仅输出 MD5 校验值（无文件名）：

`md5 -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 打印给定字符串的 MD5 校验值：

`md5 -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>`"`
