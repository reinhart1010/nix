---
layout: page
title: common/pueue-group (한국어)
description: "그룹 표시, 추가 또는 제거."
content_hash: 0a195a8639fbd827c9322e0adfbb1f0a18a45db2
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/pueue-group.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pueue-group.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pueue group

그룹 표시, 추가 또는 제거.
더 많은 정보: <https://github.com/Nukesor/pueue>.

- 모든 그룹과 그 상태 및 병렬 작업 수 표시:

`pueue group`

- 사용자 정의 그룹 추가:

`pueue group --add "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>`"`

- 그룹 제거 및 해당 작업을 기본 그룹으로 이동:

`pueue group --remove "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>`"`
