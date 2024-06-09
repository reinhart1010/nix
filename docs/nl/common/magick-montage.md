---
layout: page
title: common/magick-montage (Nederlands)
description: "Plaats afbeeldingen in een aanpasbaar raster."
content_hash: 79b325c42b2b3509675483e65382c3766e73a2d5
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/common/magick-montage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick montage

Plaats afbeeldingen in een aanpasbaar raster.
Bekijk ook: `magick`.
Meer informatie: <https://imagemagick.org/script/montage.php>.

- Plaats afbeeldingen in een raster, waarbij afbeeldingen die groter zijn dan de rastercelgrootte automatisch worden aangepast:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/montage.jpg</span>

- Plaats afbeeldingen in een raster, waarbij de rastercelgrootte automatisch wordt berekend op basis van de grootste afbeelding:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/montage.jpg</span>

- Specificeer de rastercelgrootte en pas de afbeeldingen aan om hierin te passen voordat ze worden geplaatst:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/montage.jpg</span>

- Beperk het aantal rijen en kolommen in het raster, waardoor invoerafbeeldingen over meerdere output-montages worden verdeeld:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` -tile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2x3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">montage_%d.jpg</span>

- Wijzig de grootte en snijd afbeeldingen bij om hun rastercellen te vullen voordat ze worden geplaatst:

`magick montage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...</span>` -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+0+0</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480^</span>` -gravity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">center</span>` -crop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480+0+0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/montage.jpg</span>
