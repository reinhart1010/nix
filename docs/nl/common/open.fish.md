---
layout: page
title: common/open.fish (Nederlands)
description: "Opent bestanden, mappen en URI's met standaardtoepassingen."
content_hash: 02d2e631011ac9c708271ace62b69675a426d6d9
last_modified_at: 2024-03-10
related_topics:
  - title: English version
    url: /en/common/open.fish.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/open.fish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

Opent bestanden, mappen en URI's met standaardtoepassingen.
Deze commando is beschikbaar via fish op besturingssystemen zonder het ingebouwde `open`-commando (bijv. Haiku en macOS).
Meer informatie: <https://fishshell.com/docs/current/cmds/open.html>.

- Open een bestand met de bijbehorende applicatie:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.ext</span>

- Open alle bestanden van een bepaalde extensie in de huidige map met de bijbehorende toepassing:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- Open een map met behulp van de standaardbestandbeheerder:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Open een website met behulp van de standaard webbrowser:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Open een specifieke URI met behulp van de standaardtoepassing die deze aankan:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
