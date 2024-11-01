---
layout: page
title: common/kubectl-delete (한국어)
description: "Kubernetes 리소스 삭제."
content_hash: e87f32e0f261bd780af9598f557e77c2a14c628a
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-delete.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl-delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl delete

Kubernetes 리소스 삭제.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- 특정 포드 삭제:

`kubectl delete pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>

- 특정 배포 삭제:

`kubectl delete deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">배포_이름</span>

- 특정 노드 삭제:

`kubectl delete node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>

- 지정된 네임스페이스의 모든 포드 삭제:

`kubectl delete pods --all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 지정된 네임스페이스의 모든 배포 및 서비스 삭제:

`kubectl delete deployments,services --all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 모든 노드 삭제:

`kubectl delete nodes --all`

- YAML 매니페스트에 정의된 리소스 삭제:

`kubectl delete --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트.yaml</span>
