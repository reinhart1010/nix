---
layout: page
title: windows/bleachbit_console (Nederlands)
description: "Verwijder overbodige bestanden op het bestandssysteem."
content_hash: 03c1cf8ec05fc0e9fb41a055fbf4987070348fcb
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/windows/bleachbit_console.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bleachbit_console

Verwijder overbodige bestanden op het bestandssysteem.
Meer informatie: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start de grafische gebruikersinterface (GUI) van Bleachbit:

`bleachbit_console.exe --gui`

- Versnipper een bestand:

`bleachbit_console.exe --shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon beschikbare schoonmaakopties:

`bleachbit_console.exe --list-cleaners`

- Bekijk een voorbeeld van de bestanden die zullen worden verwijderd en andere wijzigingen voordat de schoonmaak-operatie wordt uitgevoerd:

`bleachbit_console.exe --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>

- Voer de schoonmaakoperatie uit en verwijder bestanden:

`bleachbit_console.exe --clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>
