---
layout: page
title: common/knife (English)
description: "Interact with a Chef server from a local Chef repo."
content_hash: 3383b3302fd5f449083089bcdc7a1c4aac6a7968
last_modified_at: 2023-07-16
---
# knife

Interact with a Chef server from a local Chef repo.
More information: <https://docs.chef.io/knife.html>.

- Bootstrap a new node:

`knife bootstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fqdn_or_ip</span>

- List all registered nodes:

`knife node list`

- Show a node:

`knife node show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>

- Edit a node:

`knife node edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_name</span>

- Edit a role:

`knife role edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_name</span>

- View a data bag:

`knife data bag show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_bag_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_bag_item</span>

- Upload a local cookbook to the Chef server:

`knife cookbook upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookbook_name</span>
