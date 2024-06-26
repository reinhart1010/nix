---
layout: page
title: common/telnet (Nederlands)
description: "Maak verbinding met een opgegeven poort van een host met behulp van het telnet-protocol."
content_hash: 5decff1d3150142559ab459bf4a30fceeac9cc94
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/common/telnet.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/telnet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# telnet

Maak verbinding met een opgegeven poort van een host met behulp van het telnet-protocol.
Meer informatie: <https://manned.org/telnet>.

- Telnet naar de standaardpoort van een host:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Telnet naar een specifieke poort van een host:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Beëindig een telnet-sessie:

`quit`

- Verstuur de standaard escape-tekencombinatie om de sessie te beëindigen:

`<Ctrl> + ]`

- Start `telnet` met "x" als het sessie beëindigingsteken:

`telnet -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Telnet naar de Star Wars-animatie:

`telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">towel.blinkenlights.nl</span>
