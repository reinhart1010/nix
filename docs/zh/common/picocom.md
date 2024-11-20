---
layout: page
title: common/picocom (中文)
description: "模拟串行端口的极简程序。"
content_hash: efa3f19b79a3a05350cb9712a8a66d8b7da935dd
last_modified_at: 2024-11-20
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
tldri18n_status: 2
---
# picocom

模拟串行端口的极简程序。
更多信息：<https://manned.org/picocom>.

- 以指定波特率连接到串行端口：

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">波特率</span>

- 映射特殊字符（例如：将 LF 映射为 CRLF）：

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf</span>
