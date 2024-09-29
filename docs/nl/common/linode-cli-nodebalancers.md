---
layout: page
title: common/linode-cli-nodebalancers (Nederlands)
description: "Beheer Linode NodeBalancers."
content_hash: 8f635e09b324a65b5c39b968c01f5bca59ca51c1
last_modified_at: 2024-09-29
related_topics:
  - title: English version
    url: /en/common/linode-cli-nodebalancers.html
    icon: bi bi-globe
tldri18n_status: 2
---
# linode-cli nodebalancers

Beheer Linode NodeBalancers.
Bekijk ook: `linode-cli`.
Meer informatie: <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>.

- Toon alle NodeBalancers:

`linode-cli nodebalancers list`

- Maak een nieuwe NodeBalancer:

`linode-cli nodebalancers create --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regio</span>

- Toon details van een specifieke NodeBalancer:

`linode-cli nodebalancers view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- Update een bestaande NodeBalancer:

`linode-cli nodebalancers update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>` --label `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuw_label</span>

- Verwijder een NodeBalancer:

`linode-cli nodebalancers delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- Toon alle configuraties voor een NodeBalancer:

`linode-cli nodebalancers configs list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>

- Voeg een nieuwe configuratie toe aan een NodeBalancer:

`linode-cli nodebalancers configs create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nodebalancer_id</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` --protocol `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol</span>
