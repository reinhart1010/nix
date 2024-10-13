---
layout: page
title: common/date (한국어)
description: "시스템 날짜 설정 및 표시."
content_hash: fcafd51a0e20d308f7eb60bfa612a0885d1b8fa5
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/date.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/date.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/date.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/date.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

시스템 날짜 설정 및 표시.
더 많은 정보: <https://www.gnu.org/software/coreutils/date>.

- 기본 로컬 형식을 사용하여 현재 날짜 표시:

`date +%c`

- 현재 날짜를 UTC 및 ISO 8601 형식으로 표시:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- 현재 날짜를 Unix 타임스탬프로 표시 (Unix epoch 이후 몇 초):

`date +%s`

- 기본 형식을 사용하여 특정 날짜 표시(Unix 타임스탬프로 표시):

`date -d @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1473305798</span>

- 특정 날짜를 Unix 타임스탬프 형식으로 변환:

`date -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2018-09-01 00:00</span>`" +%s --utc`

- 현재 날짜를 RFC-3339 형식으로 표시 (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339 s`

- `MMDDhhmmYYYY.ss` (`YYYY` 와 `.ss`는 선택 사항) 형식을 사용해 현재 날짜를 설정:

`date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">093023592021.59</span>

- ISO 기준 현재 몇 번째 주인지 표시:

`date +%V`
