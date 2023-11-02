---
layout: page
title: common/magick (Nederlands)
description: "Creër, bewerk, vorm, of converteer bitmapafbeeldingen."
content_hash: ad424a0ec49cbe0b5baa7c546c8330fe0d1bf23d
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/common/magick.html
    icon: bi bi-globe
---
# magick

Creër, bewerk, vorm, of converteer bitmapafbeeldingen.
ImageMagick versie 7+. Bekijk `convert` voor versies 6 en lager.
Meer informatie: <https://imagemagick.org/>.

- Converteer bestandstype:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.jpg</span>

- Formaat van een afbeelding wijzigen, maak een nieuw kopie:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.png</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.jpg</span>

- Creër een GIF door middel van afbeeldingen:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.gif</span>

- Creër een dambordpatroon:

`magick -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480</span>` pattern:checkerboard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/dambordpatroon.png</span>

- Converteer afbeeldingen naar individuele PDF-pagina's:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -adjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pagina-%d.pdf</span>
