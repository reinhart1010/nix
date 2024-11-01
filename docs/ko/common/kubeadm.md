---
layout: page
title: common/kubeadm (한국어)
description: "Kubernetes 클러스터를 생성하고 관리하기 위한 명령줄 인터페이스."
content_hash: 034e8da6343e3b5e936d4df1201d33561eba043b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/kubeadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubeadm

Kubernetes 클러스터를 생성하고 관리하기 위한 명령줄 인터페이스.
더 많은 정보: <https://kubernetes.io/docs/reference/setup-tools/kubeadm>.

- Kubernetes 마스터 노드 생성:

`kubeadm init`

- Kubernetes 워커 노드를 부트스트랩하고 클러스터에 가입:

`kubeadm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>

- TTL이 12시간인 새로운 부트스트랩 토큰 생성:

`kubeadm token create --ttl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">12h0m0s</span>

- Kubernetes 클러스터가 업그레이드 가능한지와 사용 가능한 버전 확인:

`kubeadm upgrade plan`

- 지정된 버전으로 Kubernetes 클러스터 업그레이드:

`kubeadm upgrade apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 클러스터의 구성이 포함된 kubeadm ConfigMap 보기:

`kubeadm config view`

- 'kubeadm init' 또는 'kubeadm join'으로 호스트에 적용된 변경사항 되돌리기:

`kubeadm reset`
