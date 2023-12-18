---
layout: page
title: common/pamtotiff (Nederlands)
description: "Converteer een PAM afbeelding naar een TIFF bestand."
content_hash: b76423cfa1906abe157e1e4d7f9036252b8cba89
last_modified_at: 2023-12-18
related_topics:
  - title: English version
    url: /en/common/pamtotiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamtotiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamtotiff

Converteer een PAM afbeelding naar een TIFF bestand.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamtotiff.html>.

- Converteer een PAM afbeelding naar een TIFF afbeelding:

`pamtotiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.tiff</span>

- Specificeer expliciet de compressie methode voor een uitvoerbestand:

`pamtotiff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|packbits|lzw|g3|g4|flate|adobeflate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.tiff</span>

- Produceer altijd een gekleurde TIFF afbeelding, ook als de invoer afbeelding een grijsschaal is:

`pamtotiff -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.tiff</span>
