---
layout: page
title: common/ac (한국어)
description: "사용자들이 시스템에 얼마나 오랫동안 접속해 있는지에 대한 통계 정보를 표시."
content_hash: b1c64bd222936b501b7d12e136c36f07850817c9
last_modified_at: 2023-09-20
related_topics:
  - title: English version
    url: /en/common/ac.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ac.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ac.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ac

사용자들이 시스템에 얼마나 오랫동안 접속해 있는지에 대한 통계 정보를 표시.
더 많은 정보: <https://man.openbsd.org/ac>.

- 현재 사용자의 연결된 시간을 시간 단위로 출력:

`ac`

- 모든 사용자의 연결된 시간을 시간 단위로 출력:

`ac -p`

- 특정 사용자의 연결된 시간을 시간 단위로 출력:

`ac -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>

- 특정 사용자의 연결된 시간을 평균 시간과 총 접속 시간을 일 단위로 출력:

`ac -dp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>
