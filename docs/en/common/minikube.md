---
layout: page
title: common/minikube (English)
description: "Tool to run Kubernetes locally."
content_hash: 046d238ee78f9dc78c2cdc787ca496f4f6a1b6d2
last_modified_at: 2023-07-17
---
# minikube

Tool to run Kubernetes locally.
More information: <https://github.com/kubernetes/minikube>.

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
