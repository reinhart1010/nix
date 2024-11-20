---
layout: page
title: common/uudecode (中文)
description: "解码被 `uuencode` 编码的文件。"
content_hash: c42b8201c68a1946ebce648e1c7bf4673c6f1f9c
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/uudecode.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uudecode.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uudecode

解码被 `uuencode` 编码的文件。
更多信息：<https://manned.org/uudecode>.

- 解码用 `uuencode` 编码的文件，并将结果打印到 `stdout`：

`uudecode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/编码文件</span>

- 解码用 `uuencode` 编码的文件，并将结果写入到一个文件中：

`uudecode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/解码文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/编码文件</span>
