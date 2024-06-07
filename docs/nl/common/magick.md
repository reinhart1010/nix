---
layout: page
title: common/magick (Nederlands)
description: "Creër, bewerk, vorm of converteer bitmapafbeeldingen."
content_hash: 7b281879c7f85f8fb8c6e0a677822ff238c2fe3a
last_modified_at: 2024-06-07
related_topics:
  - title: English version
    url: /en/common/magick.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick

Creër, bewerk, vorm of converteer bitmapafbeeldingen.
Deze tool vervangt `convert` in ImageMagick 7+. Bekijk `magick convert` om de oude tool te gebruiken in versies 7+.
Sommige subcommando's zoals `mogrify` hebben hun eigen documentatie.
Meer informatie: <https://imagemagick.org>.

- Converteer tussen afbeeldingsformaten:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.jpg</span>

- Wijzig de grootte van een afbeelding en maak een nieuwe kopie:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/invoer_afbeelding.png</span>` -resize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100x100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.jpg</span>

- Maak een GIF van alle JPEG-afbeeldingen uit de huidige map:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_afbeelding.gif</span>

- Creër een dambordpatroon:

`magick -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640x480</span>` pattern:checkerboard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/dambordpatroon.png</span>

- Maak een PDF van alle JPEG-afbeeldingen uit de huidige map:

`magick `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` -adjoin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pagina-%d.pdf</span>
