---
layout: page
title: linux/bleachbit (Nederlands)
description: "Verwijder overbodige bestanden op het bestandssysteem."
content_hash: 42de21c6c160cc35897a42cfe93098430d303986
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/linux/bleachbit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bleachbit

Verwijder overbodige bestanden op het bestandssysteem.
Meer informatie: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start de grafische gebruikersinterface (GUI) van Bleachbit:

`bleachbit --gui`

- Versnipper een bestand:

`bleachbit --shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon beschikbare schoonmaakopties:

`bleachbit --list-cleaners`

- Bekijk een voorbeeld van de bestanden die zullen worden verwijderd en andere wijzigingen die worden doorgevoerd voordat de schoonmaakoperatie wordt uitgevoerd:

`bleachbit --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>

- Voer de schoonmaakoperatie uit en verwijder bestanden:

`bleachbit --clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>
