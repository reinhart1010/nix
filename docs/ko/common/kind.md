---
layout: page
title: common/kind (한국어)
description: "Docker 컨테이너 \"노드\"를 사용하여 로컬 Kubernetes 클러스터를 실행."
content_hash: 8f6ea04fba92c9f698eea826b19fc3d3968c70f1
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kind.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kind.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kind

Docker 컨테이너 "노드"를 사용하여 로컬 Kubernetes 클러스터를 실행.
Kubernetes 자체 테스트를 위해 설계되었으나, 로컬 개발이나 지속적 통합에도 사용 가능.
더 많은 정보: <https://github.com/kubernetes-sigs/kind>.

- 로컬 Kubernetes 클러스터 생성:

`kind create cluster --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 하나 이상의 클러스터 삭제:

`kind delete clusters `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">클러스터_이름</span>

- 클러스터, 노드 또는 kubeconfig에 대한 세부 정보 가져오기:

`kind get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clusters|nodes|kubeconfig</span>

- kubeconfig 또는 로그 내보내기:

`kind export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kubeconfig|logs</span>
