---
layout: page
title: common/az-advisor (한국어)
description: "Azure 구독 정보를 관리."
content_hash: 6776a0e870e3ce6bce7ab3db998e7c02613872ec
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/common/az-advisor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-advisor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az advisor

Azure 구독 정보를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/advisor>.

- 전체 구독에 대한 Azure Advisor 구성을 나열:

`az advisor configuration list`

- 지정된 구독 또는 리소스 그룹에 대한 Azure Advisor 구성을 표시:

`az advisor configuration show --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- Azure Advisor 권장사항 나열:

`az advisor recommendation list`

- Azure Advisor 권장사항 활성화:

`az advisor recommendation enable --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- Azure Advisor 권장사항 비활성화:

`az advisor recommendation disable --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>
