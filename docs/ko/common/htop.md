---
layout: page
title: common/htop (한국어)
description: "실행 중인 프로세스에 대한 동적 실시간 정보를 표시합니다. `top`의 향상된 버전입니다."
content_hash: b0be2219e51f104441cd91b86e51c81f56f0b5d6
last_modified_at: 2023-10-20
related_topics:
  - title: English version
    url: /en/common/htop.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/htop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/htop.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># htop

실행 중인 프로세스에 대한 동적 실시간 정보를 표시합니다. `top`의 향상된 버전입니다.
더 많은 정보: <https://htop.dev/>.

- `htop` 시작:

`htop`

- 특정 사용자가 소유한 프로세스를 표시하는 `htop`을 시작합니다:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 이름</span>

- 지정된 `sort_item`을 기준으로 프로세스를 정렬합니다(사용 가능한 옵션을 보려면 `htop --sort help`을 사용):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort_item</span>

- 업데이트 사이에 지정된 지연(10분의 1초)으로 `htop`을 시작(예: 50 = 5초):

`htop --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- htop을 실행하는 동안 대화형 명령 확인:

`?`

- 다른 탭으로 전환:

`tab`

- 도움말 표시:

`htop --help`
