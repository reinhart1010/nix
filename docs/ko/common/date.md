---
layout: page
title: common/date (한국어)
description: "시스템 날짜 설정 및 표시."
content_hash: 3b0084098fa2e8d9a58d01d26045273dbc31db55
related_topics:
  - title: English version
    url: /en/common/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/date.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/date.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/date.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># date

시스템 날짜 설정 및 표시.
더 많은 정보: <https://www.gnu.org/software/coreutils/date>.

- 기본 로컬 형식을 사용하여 현재 날짜 표시:

`date +"%c"`

- 현재 날짜를 UTC 및 ISO 8601 형식으로 표시:

`date -u +"%Y-%m-%dT%H:%M:%SZ"`

- 현재 날짜를 Unix 타임스탬프로 표시 (Unix epoch 이후 몇 초):

`date +%s`

- 기본 형식을 사용하여 특정 날짜 표시(Unix 타임스탬프로 표시):

`date -d @1473305798`

- 특정 날짜를 Unix 타임스탬프 형식으로 변환:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`
