---
layout: page
title: common/cut (한국어)
description: "`stdin` 혹은 파일에서 출력 필드를 자른다."
content_hash: 484508fe864ddddbad14eef0b1e128b289f1452c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cut.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cut.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cut.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cut

`stdin` 혹은 파일에서 출력 필드를 자른다.
더 많은 정보: <https://www.gnu.org/software/coreutils/cut>.

- `stdin`의 각 라인에 첫번째 16개의 문자를 자르기:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-16</span>

- 지정된 파일의 각 라인의 첫번째 16개 문자를 자르기:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 3번째 문자 부터 각 라인의 끝까지 모든 문자를 자르기:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-</span>

- `:` 을 필드 구분 기호로 사용하여 각 라인의 5번째 필드를 자르기(기본 구분 기호 : 탭):

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- `;` 을 구분 기호로 사용하여 각 라인의 2번째와 10번째 필드를 자르기:

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,10</span>

- 공백을 구분 기호로 사용하여 각 라인의 끝까지 필드 3을 자르기:

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> </span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-</span>
