---
layout: page
title: common/kube-capacity (한국어)
description: "Kubernetes 클러스터의 리소스 요청, 제한 및 활용 개요 제공."
content_hash: d84d52454474345a41e6cc031a5e1e6d2bb4f51f
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/kube-capacity.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kube-capacity.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kube-capacity

Kubernetes 클러스터의 리소스 요청, 제한 및 활용 개요 제공.
`kubectl top`과 `kubectl describe`의 장점을 결합하여 클러스터 리소스에 초점을 맞춘 CLI.
더 많은 정보: <https://github.com/robscott/kube-capacity>.

- 노드를 나열하고 총 CPU 및 메모리 리소스 요청 및 제한 포함:

`kube-capacity`

- 파드 포함:

`kube-capacity -p`

- 활용도 포함:

`kube-capacity -u`
