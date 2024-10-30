---
layout: page
title: common/dolt-gc (한국어)
description: "더 이상 참조되지 않거나, 더 이상 필요하지 않은 데이터를 저장소에서 검색."
content_hash: a483ab5a5b7425db8b11a958fcdc95fd22d663c3
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/dolt-gc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dolt-gc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dolt-gc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dolt gc

더 이상 참조되지 않거나, 더 이상 필요하지 않은 데이터를 저장소에서 검색.
더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-gc>.

- 저장소에서 참조되지 않은 데이터를 정리:

`dolt gc`

- 더 빠르지만 덜 철저한 가비지 수집 프로세스를 시작:

`dolt gc --shallow`
