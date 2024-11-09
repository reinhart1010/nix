---
layout: page
title: common/topydo (한국어)
description: "todo.txt 형식을 사용하는 할 일 목록 애플리케이션."
content_hash: fc92e476739801d03b9e8475fd67460d0cc56a83
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/topydo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/topydo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/topydo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># topydo

todo.txt 형식을 사용하는 할 일 목록 애플리케이션.
더 많은 정보: <https://github.com/topydo/topydo>.

- 특정 프로젝트와 주어진 컨텍스트로 할 일 추가:

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">할일_메시지</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨텍스트_이름</span>`"`

- 마감일이 내일이고 우선순위가 `A`인 할 일 추가:

`topydo add "(A) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">할일_메시지</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1d</span>`"`

- 마감일이 금요일인 할 일 추가:

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">할일_메시지</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fri</span>`"`

- 비엄격한 반복 할 일 추가 (다음 마감일 = 지금 + 반복):

`topydo add "물 주기 due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mon</span>` rec:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1w</span>`"`

- 엄격한 반복 할 일 추가 (다음 마감일 = 현재 마감일 + 반복):

`topydo add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">할일_메시지</span>` due:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-01-01</span>` rec:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+1m</span>`"`

- 마지막으로 실행한 `topydo` 명령 되돌리기:

`topydo revert`
