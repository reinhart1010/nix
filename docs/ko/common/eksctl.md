---
layout: page
title: common/eksctl (한국어)
description: "Amazon EKS의 공식 CLI."
content_hash: ce46eb208bd4ad170a47aa3007abcf6e1afbb71b
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/eksctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eksctl

Amazon EKS의 공식 CLI.
더 많은 정보: <https://eksctl.io>.

- 기본 클러스터 생성:

`eksctl create cluster`

- 클러스터 또는 모든 클러스터에 대한 세부 정보를 나열:

`eksctl get cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --region=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>

- 파일의 모든 구성 정보를 전달하는 클러스터를 생성:

`eksctl create cluster --config-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 구성 파일을 사용하여 클러스터를 생성하고, 나중에까지 노드 그룹 생성을 건너뜀:

`eksctl create cluster --config-file=<path> --without-nodegroup`

- 클러스터 삭제:

`eksctl delete cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --region=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>

- 클러스터를 생성하고, 기본값이 아닌 다른 파일에 클러스터 자격 증명을 사용:

`eksctl create cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --kubeconfig=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.yaml</span>

- 클러스터를 생성하고, 클러스터 자격 증명을 로컬에 저장하지 않도록 방지:

`eksctl create cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --write-kubeconfig=false`

- 클러스터를 생성하고 `eksctl`이 `~/.kube/eksctl/clusters` 디렉터리에서 클러스터 자격 증명을 관리:

`eksctl create cluster --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --nodes=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --auto-kubeconfig`
