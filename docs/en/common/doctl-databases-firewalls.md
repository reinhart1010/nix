---
layout: page
title: common/doctl-databases-firewalls (English)
description: "Manage firewalls for database clusters."
content_hash: 94fbe320b7e9090f46897365a270828511ffdd35
last_modified_at: 2023-10-12
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># doctl databases firewalls

Manage firewalls for database clusters.
More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls>.

- Run a `doctl databases firewalls` command with an access token:

`doctl databases firewalls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">access_token</span>

- Retrieve a list of firewall rules for a given database:

`doctl databases firewalls list`

- Add a database firewall rule to a given database:

`doctl databases firewalls append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` --rule `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">droplet|k8s|ip_addr|tag|app</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">value</span>

- Remove a firewall rule for a given database:

`doctl databases firewalls remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_uuid</span>
