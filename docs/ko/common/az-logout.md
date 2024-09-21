---
layout: page
title: common/az-logout (한국어)
description: "Azure 구독에서 로그아웃."
content_hash: b558be0552100be086168c47bfa3cf8164bc08a2
last_modified_at: 2024-09-21
related_topics:
  - title: Deutsch version
    url: /de/common/az-logout.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/az-logout.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-logout.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-logout.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az logout

Azure 구독에서 로그아웃.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/reference-index#az_logout>.

- 활성 계정에서 로그아웃:

`az logout`

- 특정 사용자 이름을 로그아웃:

`az logout --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias@somedomain.com</span>
