---
layout: page
title: common/minikube (English)
description: "Tool to run Kubernetes locally."
content_hash: 754b22126c053d528742f832047997c40dc66d2a
last_modified_at: 2024-02-08
tldri18n_status: 2
---
# minikube

Tool to run Kubernetes locally.
More information: <https://minikube.sigs.k8s.io/docs/>.

- Start the cluster:

`minikube start`

- Get the IP address of the cluster:

`minikube ip`

- Access a service named my_service exposed via a node port and get the URL:

`minikube service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_service</span>` --url`

- Open the Kubernetes dashboard in a browser:

`minikube dashboard`

- Stop the running cluster:

`minikube stop`

- Delete the cluster:

`minikube delete`

- Connect to LoadBalancer services:

`minikube tunnel`
