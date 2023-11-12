---
layout: page
title: common/kubectl-logs (Deutsch)
description: "Logs für Container in einem Pod anzeigen."
content_hash: 9b0ab5362ad52cbf6a5dd8a3cbbf32cc57c9a95b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/kubectl-logs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl logs

Logs für Container in einem Pod anzeigen.
Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

- Zeige Logs für einen Einzelcontainer-Pod an:

`kubectl logs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Zeige Logs für einen bestimmten Container in einem Pod an:

`kubectl logs --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Zeige Logs für alle Container in einem Pod an:

`kubectl logs --all-containers=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Folge den Pod-Logs (stream):

`kubectl logs --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Folge den Pod-Logs (stream) für einen bestimmten Container in einem Pod:

`kubectl logs --follow --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Zeige Pod-Logs die neuer einer relativen Zeit sind `10s`, `5m`, or `1h`:

`kubectl logs --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">relative_time</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Zeige die 10 neuesten Logzeilen in einem Pod:

`kubectl logs --tail=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>
