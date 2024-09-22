---
layout: page
title: common/az-group (한국어)
description: "리소스 그룹 및 템플릿 배포를 관리."
content_hash: b7941a0acf9c5f7e9acaad6f5dcc821761d70c37
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/az-group.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/az-group.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az group

리소스 그룹 및 템플릿 배포를 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/group>.

- 새로운 리소스 그룹 생성:

`az group create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치</span>

- 리소스 그룹이 있는지 확인:

`az group exists --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 리소스 그룹 삭제:

`az group delete --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 리소스 그룹의 조건이 충족될 때까지 기다림:

`az group wait --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">created|deleted|exists|updated</span>
