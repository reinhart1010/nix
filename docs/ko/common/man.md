---
layout: page
title: common/man (한국어)
description: "설명서 페이지 형식 지정 및 표시."
content_hash: 10974cf4f201ddaa9b6f389ef2151ca520039c08
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/man.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/man.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/man.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# man

설명서 페이지 형식 지정 및 표시.
더 많은 정보: <https://www.manned.org/man>.

- 명령에 대한 설명서 페이지를 표시:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 섹션 7의 명령에 대한 설명서 페이지를 표시:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 명령에 사용 가능한 모든 섹션 나열:

`man -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 설명서 페이지 검색 경로 표시:

`man --path`

- 설명서 페이지 자체가 아닌 설명서 페이지의 위치를 표시:

`man -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 특정 로케일을 사용하여 설명서 페이지 표시:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>

- 검색 문자열이 포함된 설명서 페이지 검색:

`man -k "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_문자열</span>`"`
