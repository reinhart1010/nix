---
layout: page
title: common/pnmquant (Nederlands)
description: "Kwantiseer de kleuren in een PNM afbeelding naar een kleinere set."
content_hash: 3ca3e04f17ad2c67debda799fdf95d8a5d23f510
last_modified_at: 2023-12-21
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pnmquant.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pnmquant

Kwantiseer de kleuren in een PNM afbeelding naar een kleinere set.
Dit commando is een combinatie van `pnmcolormap` en `pnmremap` en accepteert de combinatie van hun opties, behalve `-mapfile`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- Genereer een afbeelding door alleen gebruik te maken van `n_kleuren` of minder kleuren zo dichtbij mogelijk van de invoerafbeelding:

`pnmquant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kleuren</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer.pnm</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pnm</span>
