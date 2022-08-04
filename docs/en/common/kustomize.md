---
layout: page
title: common/kustomize (English)
description: "Kustomize is a tool to easily deploy resources for Kubernetes."
content_hash: 0d94b72f78aad159ed28ed8d30b208c5e7513055
---
# kustomize

Kustomize is a tool to easily deploy resources for Kubernetes.
More information: <https://github.com/kubernetes-sigs/kustomize>.

- Create kustomization file with resources and namespace:

`kustomize create --resources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment.yaml,service.yaml</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">staging</span>

- Build kustomization file and deploy it with `kubectl`:

`kustomize build . | kubectl apply -f -`

- Set an image in the kustomization file:

`kustomize edit set image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">busybox=alpine:3.6</span>

- Search for Kubernetes resources in the current directory to be added to the kustomization file:

`kustomize create --autodetect`
