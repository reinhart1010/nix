---
layout: page
title: common/popeye (English)
description: "Report potential issues with Kubernetes deployment manifests."
content_hash: 1c4aaf2c3cc2b44bbb6cd2d37f4c06af1f110f78
last_modified_at: 2024-02-15
tldri18n_status: 2
---
# popeye

Report potential issues with Kubernetes deployment manifests.
More information: <https://github.com/derailed/popeye>.

- Scan the current Kubernetes cluster:

`popeye`

- Scan a specific namespace:

`popeye -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Scan specific Kubernetes context:

`popeye --context=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context</span>

- Use a spinach configuration file for scanning:

`popeye -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spinach.yaml</span>
