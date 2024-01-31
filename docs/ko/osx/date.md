---
layout: page
title: osx/date (한국어)
description: "시스템 날짜 설정 또는 표시."
content_hash: 6d7c37a207fd581b7619780068aa467a0cd56e73
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

시스템 날짜 설정 또는 표시.
더 많은 정보: <https://keith.github.io/xcode-man-pages/date.1.html>.

- 기본 로케일 형식을 사용하여 현재 날짜를 표시:

`date +%c`

- 현재 날짜를 UTC 및 ISO 8601 형식으로 표시:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- 현재 날짜를 Unix 타임스탬프(Unix 간격 이후초)로 표시:

`date +%s`

- 기본 형식을 사용하여 특정 날짜(Unix 타임스탬프로 표시) 표시:

`date -r 1473305798`
