---
layout: page
title: common/minikube-start (한국어)
description: "다양한 설정으로 `minikube` 시작."
content_hash: 7d734dd935ff4b6c0ea5c36d51e677e0d7316ed4
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/minikube-start.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/minikube-start.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># minikube start

다양한 설정으로 `minikube` 시작.
더 많은 정보: <https://minikube.sigs.k8s.io/docs/commands/start/>.

- 특정 Kubernetes 버전으로 `minikube` 시작:

`minikube start --kubernetes-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.24.0</span>

- 특정 자원 할당(예: 메모리 및 CPU)으로 `minikube` 시작:

`minikube start --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- 특정 드라이버(예: VirtualBox)로 `minikube` 시작:

`minikube start --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualbox</span>

- 백그라운드에서 `minikube` 시작 (헤드리스 모드):

`minikube start --background`

- 사용자 지정 애드온(예: 메트릭 서버)과 함께 `minikube` 시작:

`minikube start --addons `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metrics-server</span>
