---
layout: page
title: common/pamditherbw (Nederlands)
description: "Pas dithering toe op een grijze afbeelding, zet het bijvoorbeeld om in een patroon van een zwarte en witte pixels die eruitzien als de originele grijstinten."
content_hash: 5245af9a741196d3d300d2975ebe9e2c98ba61d8
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamditherbw.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamditherbw.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamditherbw

Pas dithering toe op een grijze afbeelding, zet het bijvoorbeeld om in een patroon van een zwarte en witte pixels die eruitzien als de originele grijstinten.
Bekijk ook: `pbmreduce`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Lees een PGM afbeelding, pas dithering toe en sla het op naar een bestand:

`ppmditherbw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pgm</span>

- Gebruik de gespecificeerde kwantificering methode:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">floyd|fs|atkinson|threshold|hilbert|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pgm</span>

- Gebruik de atkinson kwantificering methode en de gespecifieerde seed voor een pseudo-random nummer generator:

`ppmditherbw -atkinson -randomseed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1337</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pgm</span>

- Specificeer de drempel waarde van de kwantificering methodes die een vorm van drempels uitvoeren:

`ppmditherbw -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fs|atkinson|thresholding</span>` -value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.pgm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.pgm</span>
