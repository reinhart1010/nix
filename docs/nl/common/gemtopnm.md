---
layout: page
title: common/gemtopnm (Nederlands)
description: "Converteer een GEM afbeelding naar een PNM afbeelding."
content_hash: 29cf80d43cb8b551241daf758300bb16f18a1cf3
last_modified_at: 2023-12-14
related_topics:
  - title: English version
    url: /en/common/gemtopnm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gemtopnm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gemtopnm

Converteer een GEM afbeelding naar een PNM afbeelding.
Meer informatie: <https://netpbm.sourceforge.net/doc/gemtopnm.html>.

- Converteer een GEM afbeelding naar een PNM afbeelding:

`gemtopnm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.img</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>

- Beschrijf de inhoud van een gespecificeerde GEM afbeelding:

`gemtopnm -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.img</span>

- Toon de versie:

`gemtopnm -version`
