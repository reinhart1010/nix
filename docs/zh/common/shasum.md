---
layout: page
title: common/shasum (中文)
description: "计算或检查加密 SHA 校验值。"
content_hash: d52c7498ed392150a8c5524a6d364fd5914c1d64
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/shasum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/shasum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># shasum

计算或检查加密 SHA 校验值。
更多信息：<https://manned.org/shasum>.

- 计算文件的 SHA1 校验值：

`shasum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 计算文件的 SHA256 校验值：

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 计算多个文件的 SHA512 校验值：

`shasum --algorithm 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名 2</span>

- 计算一个文件内列出的所有的目录文件的相对应的总数：

`shasum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">列表文件</span>

- 从标准输入中获取并计算 SHA1 校验值：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">其他命令</span>` | shasum`
