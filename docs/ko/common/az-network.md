---
layout: page
title: common/az-network (한국어)
description: "Azure 네트워크 리소스를 관리."
content_hash: c47638c8eb43f7b7889c56f17df1e616ea1f4494
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/az-network.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/az-network.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># az network

Azure 네트워크 리소스를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/network>.

- 구독 할당량에 대해 사용되는 지역의 네트워크 리소스 목록을 나열:

`az network list-usages`

- 구독의 모든 가상 네트워크를 나열:

`az network vnet list`

- 가상 네트워크 만들기:

`az network vnet create --address-prefixes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/16</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">가상네트워크</span>` --resource_group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹_이름</span>` --submet-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브넷</span>` --subnet-prefixes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0/24</span>

- 네트워크 인터페이스 카드에 대한 가속화된 네트워킹 활성화:

`az network nic update --accelerated-networking true --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네트워크_인터페이스_카드</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>
