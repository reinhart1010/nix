---
layout: page
title: common/todoist (한국어)
description: "명령줄에서 <https://todoist.com>에 접근하세요."
content_hash: b338536a57c4ee1e03e92a520a3b69071559f01c
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/todoist.html
    icon: bi bi-globe
  - title: română version
    url: /ro/common/todoist.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todoist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/todoist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># todoist

명령줄에서 <https://todoist.com>에 접근하세요.
더 많은 정보: <https://github.com/sachaos/todoist>.

- 작업 추가:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>`"`

- 라벨, 프로젝트 및 기한이 있는 높은 우선순위 작업 추가:

`todoist add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>`" --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --label-ids "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨_ID</span>`" --project-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>`" --date "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmr 9am</span>`"`

- 빠른 모드로 라벨, 프로젝트 및 기한이 있는 높은 우선순위 작업 추가:

`todoist quick '#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmr 9am</span>`" p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_이름</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨_이름</span>`'`

- 헤더 및 색상이 있는 모든 작업 나열:

`todoist --header --color list`

- 높은 우선순위의 모든 작업 나열:

`todoist list --filter p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- 지정된 라벨이 있는 오늘의 높은 우선순위 작업 나열:

`todoist list --filter '(@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라벨_이름</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">today</span>`) & p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`'`
