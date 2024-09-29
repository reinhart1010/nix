---
layout: page
title: common/linode-cli-domains (Nederlands)
description: "Beheer Linode Domains en DNS configuratie."
content_hash: c47b9afece3ec4e2233a700d028b87104713dd19
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/linode-cli-domains.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli domains

Beheer Linode Domains en DNS configuratie.
Bekijk ook: `linode-cli`.
Meer informatie: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-the-dns-manager>.

- Toon alle beheerde domeinen:

`linode-cli domains list`

- Maak een nieuw beheerd domein:

`linode-cli domains create --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_naam</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">master|slave</span>` --soa-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">email</span>

- Bekijk details van een specifiek domein:

`linode-cli domains view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_id</span>

- Verwijder een beheerd domein:

`linode-cli domains delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_id</span>

- Toon records voor een specifiek domein:

`linode-cli domains records-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_id</span>

- Voeg een DNS record toe aan een domein:

`linode-cli domains records-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_id</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|AAAA|CNAME|MX|...</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subdomein</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_value</span>

- Update een DNS record voor een domein:

`linode-cli domains records-update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">record_id</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_target_value</span>

- Verwijder een DNS record van een domein:

`linode-cli domains records-delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">record_id</span>
