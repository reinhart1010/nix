---
layout: page
title: common/kubectl-config (한국어)
description: "Kubernetes 구성(kubeconfig) 파일을 관리하여 `kubectl` 또는 Kubernetes API를 통해 클러스터에 접근할 수 있도록 함."
content_hash: 287a83c0f0910cd7d7e398abbe664953a2a48eff
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/kubectl-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubectl-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubectl config

Kubernetes 구성(kubeconfig) 파일을 관리하여 `kubectl` 또는 Kubernetes API를 통해 클러스터에 접근할 수 있도록 함.
기본적으로 Kubernetes는 `${HOME}/.kube/config`에서 구성을 가져옵니다.
같이 보기: `kubectx`, `kubens`.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config>.

- 기본 kubeconfig 파일에서 모든 컨텍스트 가져오기:

`kubectl config get-contexts`

- 사용자 지정 kubeconfig 파일에서 모든 클러스터/컨텍스트/사용자 가져오기:

`kubectl config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">get-clusters|get-contexts|get-users</span>` --kubeconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/kubeconfig.yaml</span>

- 현재 컨텍스트 가져오기:

`kubectl config current-context`

- 다른 컨텍스트로 전환:

`kubectl config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use|use-context</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨텍스트_이름</span>

- 클러스터/컨텍스트/사용자 삭제:

`kubectl config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">delete-cluster|delete-context|delete-user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cluster|context|user</span>

- 사용자 지정 kubeconfig 파일을 영구적으로 추가:

`export KUBECONFIG="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$HOME.kube/config:경로/대상/사용자/정의/kubeconfig.yaml</span>`" kubectl config get-contexts`
