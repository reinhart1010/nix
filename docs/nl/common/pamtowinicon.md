---
layout: page
title: common/pamtowinicon (Nederlands)
description: "Converteer een PAM afbeelding naar een Windows ICO bestand."
content_hash: 5c0b0f5f0362516ab0c3597eb5774505426dbc63
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/pamtowinicon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtowinicon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtowinicon

Converteer een PAM afbeelding naar een Windows ICO bestand.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamtowinicon.html>.

- Converteer een PAM afbeelding naar een ICO bestand:

`pamtowinicon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ico</span>

- Encodeer afbeeldingen met resoluties kleiner dan t in het BMP formaat en alle andere afbeeldingen in het PNG formaat:

`pamtowinicon -pngthreshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ico</span>

- Maak alle pixels buiten het doorzichtige vlak zwart:

`pamtowinicon -truetransparent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.ico</span>
