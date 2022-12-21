---
layout: page
title: common/kubectl-delete (Deutsch)
description: "Lösche Kubernetes-Ressourcen."
content_hash: 85ad34d0c57062efe635b406c3dc7a71301a2fa5
last_modified_at: 2022-12-21
related_topics:
  - title: English version
    url: /en/common/kubectl-delete.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># kubectl delete

Lösche Kubernetes-Ressourcen.
Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- Lösche einen bestimmten Pod:

`kubectl delete pod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Lösche ein bestimmtes Deployment:

`kubectl delete deployment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">deployment_name</span>

- Lösche eine bestimmte Node:

`kubectl delete node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>

- Lösche alle Pods in einem bestimmten Namespaces:

`kubectl delete pods --all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Lösche alle Deployments und Services in einem bestimmten Namespace:

`kubectl delete deployments,services --all --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Lösche alle Nodes:

`kubectl delete nodes --all`

- Lösche Resourcen, die in einer YAML Datei definiert sind:

`kubectl delete --filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/manifest.yaml</span>
