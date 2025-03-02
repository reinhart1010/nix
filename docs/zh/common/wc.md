---
layout: page
title: common/wc (中文)
description: "计数行、单词或字节。"
content_hash: cab88ccf7324d4df77d9e291a4ffe35cb31f6763
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/wc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/wc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/wc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/wc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/wc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># wc

计数行、单词或字节。
更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- 计数文件中的行数：

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 计数文件中的单词数：

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 计数文件中的字符（字节）：

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 计数文件中的字符数（考虑所有多字节的字符）：

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 使用标准输入，按顺序计数行、单词和字符（字节）：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
