---
layout: page
title: common/kubectl-describe (Deutsch)
description: "Details von Kubernetes-Objekten und -Ressourcen anzeigen."
content_hash: 927d01d5331d4a9eb75a6a65c2e6777013a4afe8
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/kubectl-describe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl describe

Details von Kubernetes-Objekten und -Ressourcen anzeigen.
Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Zeige Details zu Pods in einem bestimmten [n]amespace an:

`kubectl describe pods --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Zeige Details zu Nodes in einem bestimmten [n]amespace an:

`kubectl describe nodes --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Zeige Details zu einem bestimmten Pod in einem bestimmten [n]amespace an:

`kubectl describe pods `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Zeige Details zu einer bestimmten Node in einem bestimmten [n]amespace an:

`kubectl describe nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Zeige Details zu Ressourcen, die in einer YAML Datei definiert sind, an:

`kubectl describe --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/manifest.yaml</span>
