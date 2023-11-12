---
layout: page
title: common/kubectl-rollout (Deutsch)
description: "Verwalten des Rollouts einer Kubernetes-Ressource (deployments, daemonsets, and statefulsets)."
content_hash: bc1ed1de60dc111e455b6dd13b500b4b7f558562
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/kubectl-rollout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl rollout

Verwalten des Rollouts einer Kubernetes-Ressource (deployments, daemonsets, and statefulsets).
Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

- Starte einen rollenden Neustart einer Ressource:

`kubectl rollout restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>

- Überwache den fortlaufenden Aktualisierungsstatus einer Ressource:

`kubectl rollout status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>

- Setze eine Ressource auf die vorherige Version zurück:

`kubectl rollout undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>

- Zeige den Rollout-Verlauf einer Ressource an:

`kubectl rollout history `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_type</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource_name</span>
