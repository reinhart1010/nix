---
layout: page
title: common/minikube-start (English)
description: "Start `minikube` with different configurations."
content_hash: 459382fb5f0dd0d16145cf2dc5bbdb7b7e7fd3a0
last_modified_at: 2024-10-30
tldri18n_status: 2
---
# minikube start

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
