---
layout: page
title: common/pueue-pause (한국어)
description: "실행 중인 작업 또는 그룹 일시 중지."
content_hash: 37dd60005dbd799f33f09e4551360bdac4e55a6e
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-pause.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-pause.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue pause

실행 중인 작업 또는 그룹 일시 중지.
같이 보기: `pueue start`.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 기본 그룹의 모든 작업 일시 중지:

`pueue pause`

- 실행 중인 작업 일시 중지:

`pueue pause `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 실행 중인 작업과 그 직접적인 하위 작업 모두 일시 중지:

`pueue pause --children `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_아이디</span>

- 그룹 내 모든 작업을 일시 중지하고 새로운 작업 시작 방지:

`pueue pause --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>

- 모든 작업을 일시 중지하고 모든 그룹의 새로운 작업 시작 방지:

`pueue pause --all`
