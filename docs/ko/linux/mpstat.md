---
layout: page
title: linux/mpstat (한국어)
description: "CPU 사용 정보를 표시합니다."
content_hash: 744beca93960e74e76c96a5e4a9d732294dcdf97
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mpstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpstat

CPU 사용 정보를 표시합니다.
더 많은 정보: <https://manned.org/mpstat>.

- 2초마다 CPU 통계를 표시:

`mpstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 2초 간격으로 하나씩 5개의 보고서 표시:

`mpstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 특정 프로세서에서 2초 간격으로 하나씩 5개의 보고서 표시:

`mpstat -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
