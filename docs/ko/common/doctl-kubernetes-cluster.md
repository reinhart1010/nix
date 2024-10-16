---
layout: page
title: common/doctl-kubernetes-cluster (한국어)
description: "Kubernetes 클러스터를 관리하고 클러스터와 관련된 구성 옵션을 봄."
content_hash: 262417f0dbea09a6b1bbfbc13aae14deb69628f6
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/doctl-kubernetes-cluster.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doctl-kubernetes-cluster.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doctl kubernetes cluster

Kubernetes 클러스터를 관리하고 클러스터와 관련된 구성 옵션을 봄.
더 많은 정보: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>.

- Kubernetes 클러스터 생성:

`doctl kubernetes cluster create --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nyc1</span>` --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s-1vcpu-2gb</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 모든 Kubernetes 클러스터 나열:

`doctl kubernetes cluster list`

- kubeconfig를 가져와 저장:

`doctl kubernetes cluster kubeconfig save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 사용 가능한 업그레이드 확인:

`doctl kubernetes cluster get-upgrades `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 클러스터를 새로운 Kubernetes 버전으로 업그레이드:

`doctl kubernetes cluster upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 클러스터 삭제:

`doctl kubernetes cluster delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>
