---
layout: page
title: common/minikube-start (English)
description: "Start `minikube` with different configurations."
content_hash: 459382fb5f0dd0d16145cf2dc5bbdb7b7e7fd3a0
last_modified_at: 2024-10-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/minikube-start.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># minikube start

Start `minikube` with different configurations.
More information: <https://minikube.sigs.k8s.io/docs/commands/start/>.

- Start `minikube` with a specific Kubernetes version:

`minikube start --kubernetes-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v1.24.0</span>

- Start `minikube` with specific resource allocations (e.g., memory and CPU):

`minikube start --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>

- Start `minikube` with a specific driver (e.g., VirtualBox):

`minikube start --driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">virtualbox</span>

- Start `minikube` in the background (headless mode):

`minikube start --background`

- Start `minikube` with custom add-ons (e.g., the metrics server):

`minikube start --addons `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metrics-server</span>
