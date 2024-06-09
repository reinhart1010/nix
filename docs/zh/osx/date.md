---
layout: page
title: osx/date (中文)
description: "设置或显示系统日期。"
content_hash: 8abd3693301d4c8584d1d12225af258994abafa4
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/date.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

设置或显示系统日期。
更多信息：<https://keith.github.io/xcode-man-pages/date.1.html>.

- 使用默认区域设置的格式显示当前日期：

`date +%c`

- 以 UTC 和 ISO 8601 格式显示当前日期：

`date -u +%Y-%m-%dT%H:%M:%SZ`

- 将当前日期显示为 unix 时间戳（自 1970-01-01 00:00:00 以来的秒数）：

`date +%s`

- 使用默认格式显示特定日期（格式化指定 UNIX 时间戳）：

`date -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>
