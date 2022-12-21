---
layout: page
title: common/kubectl-get (Deutsch)
description: "Abfragen von Kubernetes Resourcen und Objekten."
content_hash: c32c5cc93619755930b9d58a6b7f3a0700f412a8
last_modified_at: 2022-12-21
related_topics:
  - title: English version
    url: /en/common/kubectl-get.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kubectl get

Abfragen von Kubernetes Resourcen und Objekten.
Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Zeige alle Namespaces im Cluster an:

`kubectl get namespaces`

- Frage alle Nodes in einem bestimmten Namespace ab:

`kubectl get nodes --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Pods in einem bestimmten Namespace ab:

`kubectl get pods --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Deployments in einem bestimmten Namespace ab:

`kubectl get deployments --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Services in einem bestimmten Namespace ab:

`kubectl get services --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Resourcen in einem bestimmten Namespace ab:

`kubectl get all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Frage alle Ressourcen ab, die in einer YAML Datei definiert sind:

`kubectl get -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/manifest.yaml</span>
