---
layout: page
title: common/az-provider (한국어)
description: "리소스 공급자 관리."
content_hash: b53e5217e495745b61de0368e39e10c38487afa9
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/az-provider.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az provider

리소스 공급자 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/provider>.

- 공급자 등록:

`az provider register --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.PolicyInsights</span>

- 공급자 등록 취소:

`az provider unregister --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.Automation</span>

- 구독에 대한 모든 공급자를 나열:

`az provider list`

- 특정 공급업체에 대한 정보를 표시:

`az provider show --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.Storage</span>

- 특정 공급자에 대한 모든 리소스 유형을 나열:

`az provider list --query "[?namespace=='`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Microsoft.Network</span>`'].resourceTypes[].resourceType"`
