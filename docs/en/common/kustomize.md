---
layout: page
title: common/kustomize (English)
description: "Easily deploy resources for Kubernetes."
content_hash: 44234b07ba70bb935696ade2538adedf8a8f2fcf
last_modified_at: 2023-11-15
tldri18n_status: 2
---
# kustomize

Easily deploy resources for Kubernetes.
More information: <https://github.com/kubernetes-sigs/kustomize>.

- Create a kustomization file with resources and namespace:

`kustomize create --resources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment.yaml,service.yaml</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">staging</span>

- Build a kustomization file and deploy it with `kubectl`:

`kustomize build . | kubectl apply -f -`

- Set an image in the kustomization file:

`kustomize edit set image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">busybox=alpine:3.6</span>

- Search for Kubernetes resources in the current directory to be added to the kustomization file:

`kustomize create --autodetect`
