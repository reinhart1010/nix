---
layout: page
title: common/az-aks (한국어)
description: "Azure Kubernetes Service (AKS) 클러스터 관리."
content_hash: 95e3e0a7930c6471a339e45db5721a1e7a88a95f
last_modified_at: 2024-09-16
related_topics:
  - title: English version
    url: /en/common/az-aks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az aks

Azure Kubernetes Service (AKS) 클러스터 관리.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/aks>.

- AKS 클러스터 나열:

`az aks list --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>

- 새로운 AKS 클러스터 생성:

`az aks create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --node-count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>` --node-vm-size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>

- AKS 클러스터 삭제:

`az aks delete --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- AKS 클러스터에 대한 접근 자격 증명을 가져옴:

`az aks get-credentials --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- AKS 클러스터에 사용할 수 있는 업그레이드 버전 가져오기:

`az aks get-upgrades --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리소스_그룹</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
