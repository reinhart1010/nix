---
layout: page
title: common/stern (English)
description: "Tail multiple pods and containers from Kubernetes."
content_hash: 916e3adb1d401504c86d1f10031485f3c0a89fa3
last_modified_at: 2023-11-20
tldri18n_status: 2
---
# stern

Tail multiple pods and containers from Kubernetes.
More information: <https://github.com/stern/stern>.

- Tail all pods within a current namespace:

`stern .`

- Tail all pods with a specific status:

`stern . --container-state `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">running|waiting|terminated</span>

- Tail all pods that matches a given regular expression:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_query</span>

- Tail matched pods from all namespaces:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_query</span>` --all-namespaces`

- Tail matched pods from 15 minutes ago:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_query</span>` --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15m</span>

- Tail matched pods with a specific label:

`stern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pod_query</span>` --selector `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">release=canary</span>
