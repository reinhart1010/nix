---
layout: page
title: common/kubectl-get (한국어)
description: "Kubernetes 객체 및 리소스 가져오기."
content_hash: 3cf86bc45fb9aae8fa9e0b7b72872f53b4ed4245
last_modified_at: 2024-11-01
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl get

Kubernetes 객체 및 리소스 가져오기.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- 현재 클러스터의 모든 네임스페이스 가져오기:

`kubectl get namespaces`

- 지정된 [n]amespace의 노드 가져오기:

`kubectl get nodes --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 지정된 [n]amespace의 파드 가져오기:

`kubectl get pods --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 지정된 [n]amespace의 배포 가져오기:

`kubectl get deployments --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 지정된 [n]amespace의 서비스 가져오기:

`kubectl get services --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- 지정된 [n]amespace의 모든 리소스 가져오기:

`kubectl get all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- YAML 매니페스트 [f]ile에 정의된 Kubernetes 객체 가져오기:

`kubectl get --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/매니페스트.yaml</span>
