---
layout: page
title: common/az-account (한국어)
description: "Azure 구독 정보를 관리."
content_hash: 8f8fb5dbd0ae902bfb740d830e53972ed4af406c
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/common/az-account.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-account.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-account.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az account

Azure 구독 정보를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/account>.

- 로그인한 계정의 모든 구독을 나열:

`az account list`

- `구독`을 햔재 활성 구독으로 설정:

`az account set --subscription `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구독_아이디</span>

- 현재 활성 구독이 지원되는 지역을 나열:

`az account list-locations`

- `MS Graph API`와 함께 사용할 액세스 토큰을 인쇄:

`az account get-access-token --resource-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ms-graph</span>

- 현재 활성화된 구독의 세부 정보를 특정 형식으로 출력:

`az account show --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|tsv|table|yaml</span>
