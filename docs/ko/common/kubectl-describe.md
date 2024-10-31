---
layout: page
title: common/kubectl-describe (한국어)
description: "Kubernetes 객체 및 리소스의 세부 정보 표시."
content_hash: 034e2d049bd142d07a427b26c1e99fd9481eed03
last_modified_at: 2024-10-31
related_topics:
  - title: Deutsch version
    url: /de/common/kubectl-describe.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/kubectl-describe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kubectl-describe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kubectl describe

Kubernetes 객체 및 리소스의 세부 정보 표시.
더 많은 정보: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- [n]amespace의 포드 세부 정보 표시:

`kubectl describe pods --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- [n]amespace의 노드 세부 정보 표시:

`kubectl describe nodes --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- [n]amespace의 특정 포드 세부 정보 표시:

`kubectl describe pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포드_이름</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- [n]amespace의 특정 노드 세부 정보 표시:

`kubectl describe nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">네임스페이스</span>

- YAML 매니페스트 [f]ile에 정의된 Kubernetes 객체의 세부 정보 표시:

`kubectl describe --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/manifest.yaml</span>
