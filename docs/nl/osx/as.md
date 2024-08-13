---
layout: page
title: osx/as (Nederlands)
description: "Draagbare GNU assembler."
content_hash: 60dd657f7f2c98e1df56eb672f22895940108265
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/osx/as.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/as.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/as.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/as.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># as

Draagbare GNU assembler.
Voornamelijk bedoeld om uitvoer van `gcc` te assembleren voor gebruik door `ld`.
Meer informatie: <https://keith.github.io/xcode-man-pages/as.1.html>.

- Assembleer een bestand en schrijf de output naar `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.s</span>

- Assembleer de output naar een specifiek bestand:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.o</span>

- Genereer sneller output door spaties en commentaarvoorverwerking over te slaan. (Moet alleen worden gebruikt voor vertrouwde compilers):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.s</span>

- Voeg een specifiek pad toe aan de lijst met mappen om te zoeken naar bestanden die zijn opgegeven in `.include`-richtlijnen:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.s</span>
