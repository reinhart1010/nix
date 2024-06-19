---
layout: page
title: osx/ping (Nederlands)
description: "Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts."
content_hash: ad4a61f5e63575cf2011a166197661c3fb3b2bb3
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/ping.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts.
Meer informatie: <https://keith.github.io/xcode-man-pages/ping.8.html>.

- Ping een specifieke host:

`ping "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostnaam</span>`"`

- Ping een host een specifiek aantal keren:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping een host, met een specifiek interval in seconden tussen de verzoeken (standaard is 1 seconde):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping een host zonder te proberen symbolische namen voor adressen op te zoeken:

`ping -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping een host en laat een bel afgaan wanneer een pakket wordt ontvangen (als je terminal dit ondersteunt):

`ping -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`

- Ping een host en toon de tijd wanneer een pakket is ontvangen (deze optie is een Apple-toevoeging):

`ping --apple-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`"`
