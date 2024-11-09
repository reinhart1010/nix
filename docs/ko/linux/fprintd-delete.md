---
layout: page
title: linux/fprintd-delete (한국어)
description: "데이터베이스에서 지문을 제거합니다."
content_hash: 56b414ee20e389f0244eb5319ffe6bedc70072b6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/fprintd-delete.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fprintd-delete.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fprintd-delete

데이터베이스에서 지문을 제거합니다.
더 많은 정보: <https://manned.org/fprintd-delete>.

- 특정 사용자의 모든 지문 제거:

`fprintd-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 특정 사용자의 특정 지문 제거:

`fprintd-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger</span>

- 도움말 표시:

`fprintd-delete`
