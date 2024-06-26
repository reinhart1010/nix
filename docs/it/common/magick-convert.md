---
layout: page
title: common/magick-convert (italiano)
description: "Strumento della suite immagineMagick per la conversione di immagini."
content_hash: 5895e9ff900c76a7fb193f414c6ceda3168e4d56
last_modified_at: 2024-06-05
related_topics:
  - title: Deutsch version
    url: /de/common/magick-convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/magick-convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/magick-convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/magick-convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/magick-convert.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># magick convert

Strumento della suite immagineMagick per la conversione di immagini.
Maggiori informazioni: <https://imagemagick.org/script/convert.php>.

- Converti un'immagine da JPEG a PNG:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>

- Scala un'immagine al 50% delle sue dimensioni originali:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>

- Scala un'immagine ad una dimensione massima di 640x480 mantenendo le proporzioni originali:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>

- Concatena più immagini orizzontalmente:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine3.png</span>` +append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine123.png</span>

- Crea una GIF da una serie di immagini con un intervallo di 100ms tra ogni immagine:

`magick convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine3.png</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">animazione.gif</span>

- Crea un'immagine a tinta unita di un determinato colore:

`magick convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>
