---
layout: page
title: common/pnmremap (Nederlands)
description: "Vervang de kleuren in een PNM afbeelding."
content_hash: 9712dd0bcbd0c24897b5eb243b19f51127c84a44
last_modified_at: 2023-12-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmremap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmremap

Vervang de kleuren in een PNM afbeelding.
Meer informatie: <https://netpbm.sourceforge.net/doc/pnmremap.html>.

- Vervang de kleuren in een afbeelding met diegene gespecificeerd in een kleurenpalet:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/kleurenpalet_bestand.ppm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>

- Gebruik Floyd-Steinberg dithering voor het representeren van missende kleuren in het kleurenpalet:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/kleurenpalet_bestand.ppm</span>` -floyd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>

- Gebruik de eerste kleur in het palet voor het representeren van missende kleuren in het kleurenpalet:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/kleurenpalet_bestand.ppm</span>` -firstisdefault `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>

- Gebruik de gespecificeerde kleur voor het representeren van de missende kleuren in het kleurenpalet:

`pnmremap -mapfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/kleurenpalet_bestand.ppm</span>` -missingcolor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kleur</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>
