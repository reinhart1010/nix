---
layout: page
title: common/pamcrater (Nederlands)
description: "Maak een PAM afbeelding van een krater terrein."
content_hash: 678c7b9ffdf5ff4f552fb79a8caeed78fd1c7755
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamcrater.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamcrater.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamcrater

Maak een PAM afbeelding van een krater terrein.
Bekijk ook: `pamshadedrelief`, `ppmrelief`.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamcrater.html>.

- Maak een afbeelding van een krater terrein met de gespecificeerde dimensies:

`pamcrater -height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hoogte</span>` -width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>

- Maak een afbeelding met het gespecificeerde nummer van kraters:

`pamcrater -number `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n_kraters</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pam</span>
