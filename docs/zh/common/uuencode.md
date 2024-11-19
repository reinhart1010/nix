---
layout: page
title: common/uuencode (中文)
description: "将二进制文件编码为 ASCII，以便通过仅支持简单 ASCII 编码的媒介传输。"
content_hash: b7fa1b410e9dd30cfd0a2897f0b6a005bcb47c1c
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/uuencode.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uuencode.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uuencode.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uuencode

将二进制文件编码为 ASCII，以便通过仅支持简单 ASCII 编码的媒介传输。
更多信息：<https://manned.org/uuencode>.

- 编码一个文件并将结果打印到 `stdout`：

`uuencode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">解码后文件名</span>

- 编码一个文件并将结果写入到一个文件：

`uuencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">解码后文件名</span>

- 使用 Base64 而不是默认的 uuencode 编码一个文件，并将结果写入到一个文件：

`uuencode -m -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">解码后文件名</span>
