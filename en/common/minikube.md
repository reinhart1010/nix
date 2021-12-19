---
layout: page
title: common/minikube (English)
description: "Tool to run Kubernetes locally."
content_hash: 5ebc1d3219014d9bf53a0dcc1e4836bb660eb22b
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
