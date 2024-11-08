---
layout: page
title: common/rbac-lookup (한국어)
description: "Kubernetes 클러스터에서 사용자, 서비스 계정 또는 그룹 이름에 연결된 역할 및 클러스터 역할을 찾습니다."
content_hash: 893d39471ccaf325e873f62046a63c8bf04ca6cd
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/rbac-lookup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rbac-lookup

Kubernetes 클러스터에서 사용자, 서비스 계정 또는 그룹 이름에 연결된 역할 및 클러스터 역할을 찾습니다.
더 많은 정보: <https://github.com/reactiveops/rbac-lookup>.

- 모든 RBAC 바인딩 보기:

`rbac-lookup`

- 주어진 표현식과 일치하는 RBAC 바인딩 보기:

`rbac-lookup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>

- 소스 역할 바인딩과 함께 모든 RBAC 바인딩 보기:

`rbac-lookup -o wide`

- 주체로 필터링된 모든 RBAC 바인딩 보기:

`rbac-lookup -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자|그룹|서비스계정</span>

- IAM 역할과 함께 모든 RBAC 바인딩 보기 (GKE를 사용하는 경우):

`rbac-lookup --gke`
