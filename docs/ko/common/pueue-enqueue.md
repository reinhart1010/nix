---
layout: page
title: common/pueue-enqueue (한국어)
description: "저장된 작업을 대기열에 추가."
content_hash: 273e11d1f4fd4630f6d079c6991fcc8e496eb7f5
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-enqueue.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-enqueue.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue enqueue

저장된 작업을 대기열에 추가.
같이 보기: `pueue stash`.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 여러 저장된 작업을 한 번에 대기열에 추가:

`pueue enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 60초 후에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 다음 수요일에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wednesday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 4개월 후에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay "4 months" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 2021-02-19에 저장된 작업을 대기열에 추가:

`pueue enqueue --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2021-02-19</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 사용 가능한 모든 날짜/시간 형식 나열:

`pueue enqueue --help`
