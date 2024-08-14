---
layout: page
title: common/ping (Nederlands)
description: "Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts."
content_hash: 01f4d05e4cc08c0e1e223d02fc419cbe0be87f3c
last_modified_at: 2024-08-14
related_topics:
  - title: Deutsch version
    url: /de/common/ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ping.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

Verstuur ICMP ECHO_REQUEST-pakketten naar netwerkhosts.
Meer informatie: <https://manned.org/ping>.

- Ping host:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping een host een specifiek aantal keren:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host met een specifiek interval in seconden tussen verzoeken (standaard is 1 seconde):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host zonder te proberen symbolische namen voor adressen op te zoeken:

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host en laat een bel afgaan wanneer een pakket wordt ontvangen (als je terminal dit ondersteunt):

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Toon ook een bericht als er geen reactie is ontvangen:

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping een host met een specifiek aantal pings, timeout (`-W`) voor elk antwoord, en totale tijdslimiet (`-w`) voor de gehele ping-uitvoering:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
