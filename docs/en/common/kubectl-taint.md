---
layout: page
title: common/kubectl-taint (English)
description: "Update the taints on nodes."
content_hash: b088bcc9af343acf9ad34953e938a106a1e64e22
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# kubectl taint

Update the taints on nodes.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint>.

- Apply taint to a node:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_value</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">effect</span>

- Remove taint from a node:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_key</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">effect</span>`-`

- Remove all taints from a node:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_key</span>`-`
