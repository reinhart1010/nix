---
layout: page
title: common/pamtotiff (Nederlands)
description: "Converteer een PAM afbeelding naar een TIFF bestand."
content_hash: b76423cfa1906abe157e1e4d7f9036252b8cba89
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/common/pamtotiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pamtotiff

Converteer een PAM afbeelding naar een TIFF bestand.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamtotiff.html>.

- Converteer een PAM afbeelding naar een TIFF afbeelding:

`pamtotiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.tiff</span>

- Specificeer expliciet de compressie methode voor een uitvoerbestand:

`pamtotiff -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|packbits|lzw|g3|g4|flate|adobeflate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.tiff</span>

- Produceer altijd een gekleurde TIFF afbeelding, ook als de invoer afbeelding een grijsschaal is:

`pamtotiff -color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_bestand.pam</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand.tiff</span>
