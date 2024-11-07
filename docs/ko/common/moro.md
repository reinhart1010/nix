---
layout: page
title: common/moro (한국어)
description: "작업 시간을 추적."
content_hash: 5374c741bd8f7f0dbaccd6749a5e599b02ecfa36
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/moro.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/moro.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># moro

작업 시간을 추적.
더 많은 정보: <https://moro.js.org>.

- 매개변수 없이 `moro`를 호출하여 현재 시간을 작업 시작 시간으로 설정:

`moro`

- 작업 시작 시간을 사용자 정의 시간으로 지정:

`moro hi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">09:30</span>

- 매개변수 없이 `moro`를 두 번째로 호출하여 현재 시간을 작업 종료 시간으로 설정:

`moro`

- 작업 종료 시간을 사용자 정의 시간으로 지정:

`moro bye `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17:30</span>

- 현재 작업일에 메모 추가:

`moro note `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3시간 프로젝트 Foo</span>

- 현재 작업일의 시간 기록 및 메모 보고서 표시:

`moro report`

- 기록된 모든 작업일의 시간 기록 및 메모 보고서 표시:

`moro report --all`
