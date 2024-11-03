---
layout: page
title: common/kops (한국어)
description: "Kubernetes 클러스터를 생성, 삭제, 업그레이드 및 유지 관리."
content_hash: b90bc8de7f61722bb9d24b63451ba77eff5cdc13
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kops.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kops

Kubernetes 클러스터를 생성, 삭제, 업그레이드 및 유지 관리.
더 많은 정보: <https://github.com/kubernetes/kops/>.

- 구성 사양에서 클러스터 생성:

`kops create cluster -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름.yaml</span>

- 새로운 SSH 공개 키 생성:

`kops create secret sshpublickey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.ssh/id_rsa.pub</span>

- 클러스터 구성을 `~/.kube/config` 파일로 내보내기:

`kops export kubecfg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 클러스터 구성을 YAML로 가져오기:

`kops get cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` -o yaml`

- 클러스터 삭제:

`kops delete cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --yes`

- 클러스터 유효성 검사:

`kops validate cluster `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>` --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">준비_시간</span>` --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필요한_검증_수</span>
