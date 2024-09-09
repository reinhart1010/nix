---
layout: page
title: common/nc (Nederlands)
description: "Netcat is een veelzijdig hulpprogramma voor het omleiden van IO naar een netwerkstream."
content_hash: e7d9a3d10c785e03422673c202f0792eda93fa5b
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/nc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nc

Netcat is een veelzijdig hulpprogramma voor het omleiden van IO naar een netwerkstream.
Meer informatie: <https://manned.org/nc>.

- Start een luisteraar op de opgegeven TCP poort en stuur er een bestand in:

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Maak verbinding met een doelluisteraar op de opgegeven poort en ontvang er een bestand uit:

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ontvangen_bestandsnaam</span>

- Scan de open TCP poorten van een opgegeven host:

`nc -v -z -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">timeout_in_seconden</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start_port</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end_port</span>

- Start een luisteraar op de opgegeven TCP poort en geef uw lokale shell toegang tot de verbonden partij (dit is gevaarlijk en kan worden misbruikt):

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_executable</span>

- Maak verbinding met een doelluisteraar en geef uw lokale shell toegang tot de externe partij (dit is gevaarlijk en kan worden misbruikt):

`nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_executable</span>

- Fungeer als een proxy en stuur gegevens door van een lokale TCP poort naar de opgegeven externe host:

`nc -l -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>` | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_port</span>

- Stuur een HTTP GET verzoek:

`echo -e "GET / HTTP/1.1\nHost: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`\n\n" | nc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>` 80`
