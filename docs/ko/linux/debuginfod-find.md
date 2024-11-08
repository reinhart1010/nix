---
layout: page
title: linux/debuginfod-find (한국어)
description: "디버그 정보 관련 데이터를 요청합니다."
content_hash: d3b9a55d8a94b082618969ea9b73cfede8a786ba
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/debuginfod-find.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/debuginfod-find.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/debuginfod-find.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># debuginfod-find

디버그 정보 관련 데이터를 요청합니다.
더 많은 정보: <https://manned.org/debuginfod-find>.

- `build_id`를 기반으로 데이터 요청:

`debuginfod-find -vv debuginfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">빌드_ID</span>
