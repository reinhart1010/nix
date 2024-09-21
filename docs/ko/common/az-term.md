---
layout: page
title: common/az-term (한국어)
description: "마켓플레이스주문을 통해 마켓플레이스 계약을 관리."
content_hash: b6adf1716abe1264935db782124f73f1e5d10c64
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/az-term.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-term.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az term

마켓플레이스주문을 통해 마켓플레이스 계약을 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/term>.

- 마켓플레이스 약관 인쇄:

`az term show --product "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제품_식별자</span>`" --plan "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랜_식별자</span>`" --publisher "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_식별자</span>`"`

- 마켓플레이스 약관에 동의:

`az term accept --product "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제품_식별자</span>`" --plan "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">플랜_식별자</span>`" --publisher "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_식별자</span>`"`
