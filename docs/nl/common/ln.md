---
layout: page
title: common/ln (Nederlands)
description: "Maakt een verwijzing naar bestanden en mappen."
content_hash: d35a62b386906db84e93812b4d0fc683b5ff763e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ln.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ln.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ln.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ln.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ln.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ln.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ln.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ln

Maakt een verwijzing naar bestanden en mappen.
Meer informatie: <https://www.gnu.org/software/coreutils/ln>.

- Maak een symbolische verwijzing naar een bestand of map:

`ln -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/bestand_of_map</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/symbolische_verwijzing</span>

- Overschrijf een bestaande symbolische verwijzing om die naar een ander bestand te verwijzen:

`ln -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/nieuw_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/symbolische_verwijzing</span>

- Maak een harde verwijzing naar een bestand:

`ln `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/harde_verwijzing</span>
