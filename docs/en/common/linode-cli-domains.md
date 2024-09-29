---
layout: page
title: common/linode-cli-domains (English)
description: "Manage Linode Domains and DNS configuration."
content_hash: f5a143ce560ccd989b417e5d26412aad1982625e
last_modified_at: 2024-09-29
related_topics:
  - title: Nederlands version
    url: /nl/common/linode-cli-domains.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli domains

Manage Linode Domains and DNS configuration.
See also: `linode-cli`.
More information: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-the-dns-manager>.

- List all managed domains:

`linode-cli domains list`

- Create a new managed domain:

`linode-cli domains create --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master|slave</span>` --soa-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- View details of a specific domain:

`linode-cli domains view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_id</span>

- Delete a managed domain:

`linode-cli domains delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_id</span>

- List records for a specific domain:

`linode-cli domains records-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_id</span>

- Add a DNS record to a domain:

`linode-cli domains records-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_id</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|AAAA|CNAME|MX|...</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomain</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_value</span>

- Update a DNS record for a domain:

`linode-cli domains records-update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">record_id</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_target_value</span>

- Delete a DNS record from a domain:

`linode-cli domains records-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">record_id</span>
