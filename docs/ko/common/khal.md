---
layout: page
title: common/khal (한국어)
description: "명령줄에서 사용하는 텍스트 기반 캘린더 및 일정 관리 애플리케이션."
content_hash: cea9e9776e692b87eb05676fdac07bb8ca806c53
last_modified_at: 2024-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/khal.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/khal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/khal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># khal

명령줄에서 사용하는 텍스트 기반 캘린더 및 일정 관리 애플리케이션.
더 많은 정보: <https://lostpackets.de/khal>.

- 상호작용 모드에서 Khal 시작:

`ikhal`

- 개인 캘린더에 예정된 다음 7일 동안의 모든 이벤트 출력:

`khal list -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>

- 개인 캘린더가 아닌 내일 10:00에 예정된 모든 이벤트 출력:

`khal at -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tomorrow</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10:00</span>

- 다음 3개월 동안의 이벤트 목록이 포함된 캘린더 출력:

`khal calendar`

- 개인 캘린더에 새 이벤트 추가:

`khal new -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2020-09-08</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:00</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">18:30</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">치과 예약</span>`"`
