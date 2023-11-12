---
layout: page
title: common/popeye (English)
description: "Utility that reports potential issues with Kubernetes deployment manifests."
content_hash: 3562e0f4284b41b639dd237a368d5d9a8d71b310
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# popeye

Utility that reports potential issues with Kubernetes deployment manifests.
More information: <https://github.com/derailed/popeye>.

- Scan the current Kubernetes cluster:

`popeye`

- Scan a specific namespace:

`popeye -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Scan specific Kubernetes context:

`popeye --context=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context</span>

- Use a spinach configuration file for scanning:

`popeye -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spinach.yaml</span>
