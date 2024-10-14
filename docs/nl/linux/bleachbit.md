---
layout: page
title: linux/bleachbit (Nederlands)
description: "Verwijder overbodige bestanden op het bestandssysteem."
content_hash: 6d81bc71fd03f930137a18d757e34691693a243a
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/bleachbit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bleachbit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bleachbit

Verwijder overbodige bestanden op het bestandssysteem.
Meer informatie: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start de grafische gebruikersinterface (GUI) van Bleachbit:

`bleachbit --gui`

- Versnipper een bestand:

`bleachbit --shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Lijst beschikbare schoonmaakopties:

`bleachbit --list-cleaners`

- Bekijk een voorbeeld van de bestanden die zullen worden verwijderd en andere wijzigingen die worden doorgevoerd voordat de schoonmaakoperatie wordt uitgevoerd:

`bleachbit --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>

- Voer de schoonmaakoperatie uit en verwijder bestanden:

`bleachbit --clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>
