---
layout: page
title: common/kubectl-get (Deutsch)
description: "Abfragen von Kubernetes Resourcen und Objekten."
content_hash: 6c3e7ea10b0a1ab58e9c01ced4a5e93b3a1e3306
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/kubectl-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl get

Abfragen von Kubernetes Resourcen und Objekten.
Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Zeige alle Namespaces im Cluster an:

`kubectl get namespaces`

- Frage alle Nodes in einem bestimmten [n]amespace ab:

`kubectl get nodes --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Pods in einem bestimmten [n]amespace ab:

`kubectl get pods --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Deployments in einem bestimmten [n]amespace ab:

`kubectl get deployments --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Services in einem bestimmten [n]amespace ab:

`kubectl get services --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Resourcen in einem bestimmten [n]amespace ab:

`kubectl get all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Ressourcen ab, die in einer YAML Datei definiert sind:

`kubectl get --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/manifest.yaml</span>
