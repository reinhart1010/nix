---
layout: page
title: common/ping6 (Nederlands)
description: "Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts via een IPv6-adres."
content_hash: 6e89434e3f9ea0416ee5dfd97734a395f435a43f
last_modified_at: 2024-06-19
related_topics:
  - title: Deutsch version
    url: /de/common/ping6.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping6.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping6.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping6

Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts via een IPv6-adres.
Meer informatie: <https://manned.org/ping6>.

- Ping een host:

`ping6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping een host een specifiek aantal keren:

`ping6 -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping een host met een specifiek interval in seconden tussen verzoeken (standaard is 1 seconde):

`ping6 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping een host zonder te proberen symbolische namen voor adressen op te zoeken:

`ping6 -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping een host en laat een bel afgaan wanneer een pakket wordt ontvangen (als je terminal dit ondersteunt):

`ping6 -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
