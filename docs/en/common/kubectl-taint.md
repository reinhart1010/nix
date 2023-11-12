---
layout: page
title: common/kubectl-taint (English)
description: "Update the taints on one or more nodes."
content_hash: c69e012de6fbc4415ade387360a4d3a515c7cf48
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kubectl taint

Update the taints on one or more nodes.
More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint>.

- Apply taint to a node:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_key</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_value</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">effect</span>

- Remove taint from a node:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_key</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">effect</span>`-`

- Remove all taints from a node:

`kubectl taint nodes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">label_key</span>`-`
