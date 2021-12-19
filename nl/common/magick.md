---
layout: page
title: common/magick (Nederlands)
description: "Creër, bewerk, vorm, of converteer bitmapafbeeldingen."
content_hash: 029064f3818e730f9a2b7efb930c62212d73011c
related_topics:
  - title: English version
    url: /en/common/magick.html
    icon: bi bi-globe
---
# magick

Creër, bewerk, vorm, of converteer bitmapafbeeldingen.
ImageMagick versie 7+. Bekijk `convert` versies 6 en lager.
Meer informatie: <https://imagemagick.org/>.

- Converteer bestandstype:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">afbeelding.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">afbeelding.jpg</span>

- Formaat van een afbeelding wijzigen, maak een nieuw kopie:

`magick convert -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">afbeelding.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">afbeelding.jpg</span>

- Creër een GIF door middel van afbeeldingen:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">afbeelding.gif</span>

- Creër een dambordpatroon:

`magick -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480</span>` pattern:checkerboard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dambordpatroon.png</span>

- Converteer afbeeldingen naar individuele PDF-pagina's:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` +adjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pagina-%d.pdf</span>
