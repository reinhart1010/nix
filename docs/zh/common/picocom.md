---
layout: page
title: common/picocom (中文)
description: "模拟串行端口的极简程序。"
content_hash: efa3f19b79a3a05350cb9712a8a66d8b7da935dd
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/picocom.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/picocom.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/picocom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/picocom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># picocom

模拟串行端口的极简程序。
更多信息：<https://manned.org/picocom>.

- 以指定波特率连接到串行端口：

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">波特率</span>

- 映射特殊字符（例如：将 LF 映射为 CRLF）：

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf</span>
