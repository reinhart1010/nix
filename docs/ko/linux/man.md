---
layout: page
title: linux/man (한국어)
description: "매뉴얼 페이지를 포맷하고 표시합니다."
content_hash: f06612d5d0893e59d174e63408505806fd01b1c1
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/man.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/man.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/man.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/man.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/man.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/man.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/man.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# man

매뉴얼 페이지를 포맷하고 표시합니다.
더 많은 정보: <https://manned.org/man>.

- 명령어에 대한 매뉴얼 페이지 표시:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 브라우저에서 명령어에 대한 매뉴얼 페이지 열기 (`BROWSER` 변수가 설정되어 있어야 함):

`man --html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 섹션 7에서 명령어에 대한 매뉴얼 페이지 표시:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령어에 대한 사용 가능한 모든 섹션 나열:

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 매뉴얼 페이지 검색 경로 표시:

`man --path`

- 매뉴얼 페이지 자체가 아닌 매뉴얼 페이지의 위치 표시:

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 특정 로케일을 사용하여 매뉴얼 페이지 표시:

`man --locale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">로케일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 검색 문자열을 포함하는 매뉴얼 페이지 검색:

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`"`
