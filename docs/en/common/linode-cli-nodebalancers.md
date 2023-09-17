---
layout: page
title: common/linode-cli-nodebalancers (English)
description: "Manage Linode NodeBalancers."
content_hash: 424fbbc7edc3213c85f8aaeacd7772d2adf4d29b
last_modified_at: 2023-09-17
---
# linode-cli nodebalancers

Manage Linode NodeBalancers.
See also: `linode-cli`.
More information: <https://www.linode.com/docs/products/tools/cli/guides/nodebalancers/>.

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
