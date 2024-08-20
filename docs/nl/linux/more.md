---
layout: page
title: linux/more (Nederlands)
description: "Toon een bestand interactief, met de mogelijkheid om te scrollen en te zoeken."
content_hash: 77526916e28c7c73dfaeb20acd36a526484b4827
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/linux/more.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/more.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># more

Toon een bestand interactief, met de mogelijkheid om te scrollen en te zoeken.
Zie ook: `less`.
Meer informatie: <https://manned.org/more>.

- Open een bestand:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon een specifieke regel:

`more +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regelnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Ga naar de volgende pagina:

`<Spatie>`

- Zoek naar een string (druk op `n` om naar de volgende overeenkomst te gaan):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">iets</span>

- Afsluiten:

`q`

- Toon hulp over interactieve commando's:

`h`
