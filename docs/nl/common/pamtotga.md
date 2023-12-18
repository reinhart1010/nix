---
layout: page
title: common/pamtotga (Nederlands)
description: "Converteer een Netpbm afbeelding naar een TrueVision Targa bestand."
content_hash: ea183aeeb0b1fbc4334592dc2d03a3e0a9500441
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/pamtotga.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtotga.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtotga

Converteer een Netpbm afbeelding naar een TrueVision Targa bestand.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamtotga.html>.

- Converteer een Netpbm afbeelding naar een TrueVision Targa bestand:

`pamtotga `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.tga</span>

- Specifieer de kleur van de uitvoer afbeelding:

`pamtotga -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cmap|cmap16|mono|rgb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.tga</span>

- Toon de versie:

`pamtotga -version`
