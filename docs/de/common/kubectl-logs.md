---
layout: page
title: common/kubectl-logs (Deutsch)
description: "Logs für Container in einem Pod anzeigen."
content_hash: b79638ae9b6e83abee7a1e4fd1a41c33a992497d
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/kubectl-logs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kubectl-logs.html
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

- Zeige Pod-Logs die neuer einer relativen Zeit sind `10s`, `5m`, or `1h`:

`kubectl logs --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">relative_time</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>

- Zeige die 10 neuesten Logzeilen in einem Pod:

`kubectl logs --tail=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_name</span>
