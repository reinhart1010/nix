---
layout: page
title: linux/mpstat (한국어)
description: "CPU 사용 정보를 표시합니다."
content_hash: 744beca93960e74e76c96a5e4a9d732294dcdf97
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mpstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mpstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mpstat

CPU 사용 정보를 표시합니다.
더 많은 정보: <https://manned.org/mpstat>.

- 2초마다 CPU 통계를 표시:

`mpstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 2초 간격으로 하나씩 5개의 보고서 표시:

`mpstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 특정 프로세서에서 2초 간격으로 하나씩 5개의 보고서 표시:

`mpstat -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
