---
layout: page
title: common/linode-cli-nodebalancers (English)
description: "Manage Linode NodeBalancers."
content_hash: e4e8e5e613c5f4dd607343ffbc3c6cb17832fb1a
last_modified_at: 2024-09-29
related_topics:
  - title: Nederlands version
    url: /nl/common/linode-cli-nodebalancers.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli nodebalancers

Manage Linode NodeBalancers.
See also: `linode-cli`.
More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>.

- List all NodeBalancers:

`linode-cli nodebalancers list`

- Create a new NodeBalancer:

`linode-cli nodebalancers create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region</span>

- View details of a specific NodeBalancer:

`linode-cli nodebalancers view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- Update an existing NodeBalancer:

`linode-cli nodebalancers update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_label</span>

- Delete a NodeBalancer:

`linode-cli nodebalancers delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- List configurations for a NodeBalancer:

`linode-cli nodebalancers configs list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- Add a new configuration to a NodeBalancer:

`linode-cli nodebalancers configs create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>
