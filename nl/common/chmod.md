---
layout: page
title: common/chmod (Nederlands)
description: "Verander de toegangstoestemmingen van een bestand of map."
content_hash: dd8511a6d17da6e03748d19bb1d29a9f373730a0
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chmod.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chmod

Verander de toegangstoestemmingen van een bestand of map.
Meer informatie: <https://www.gnu.org/software/coreutils/chmod>.

- Geef een gebruiker ([u]ser) die het bestand beheert het recht om deze uit te voeren (e[x]ecute):

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand</span>

- Geef de gebruiker ([u]ser) het recht om een bestand of map te lezen ([r]ead) en schrijven ([w]rite):

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand_of_map</span>

- Haal uitvoertoestemming (e[x]ecute) voor een bestand weg van de [g]roep:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand</span>

- Geef [a]lle gebruikers toegang om een bestand te lezen ([r]ead) en schrijven ([w]rite):

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand</span>

- Geef anderen ([o]thers) die niet in de groep van de beheerder zitten, dezelfde rechten als de [g]roep:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand</span>

- Haal alle rechten van de anderen ([o]thers) weg:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestand</span>

- Verander de toestemmingen recursief, waarbij de [g]roep en anderen ([o]thers) de mogelijkheid tot schrijven ([w]rite) krijgen:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">map</span>
