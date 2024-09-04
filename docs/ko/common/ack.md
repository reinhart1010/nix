---
layout: page
title: common/ack (한국어)
description: "프로그래머에게 최적화된 grep과 같은 검색 도구."
content_hash: aaf34ec347f33557ae944b7b47ca69d7f078f814
last_modified_at: 2024-09-04
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ack

프로그래머에게 최적화된 grep과 같은 검색 도구.
추가 정보: 훨씬 빠른 rg 명령어도 참고.
더 많은 정보: <https://beyondgrep.com/documentation>.

- 현재 디렉토리에서 문자열 또는 정규 표현식이 포함된 파일을 재귀적으로 검색:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 대소문자를 구분하지 않는 패턴 검색:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 패턴과 일치하는 줄을 검색해, 검색되어 일치하는 텍스트만([o]nly) 인쇄:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 특정 타입을 가지는 파일로 검색을 제한:

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 특정 타입을 가지는 파일을 검색하지 않음:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 패턴과 일치하는 총 항목 수를 계산:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 각 파일에 대해서, 파일 이름과 일치하는 개수를 출력:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- `--type`과 함께 사용할 수 있는 모든 값을 나열:

`ack --help-types`
