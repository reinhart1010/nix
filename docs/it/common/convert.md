---
layout: page
title: common/convert (italiano)
description: "Strumento della suite immagineMagick per la conversione di immagini."
content_hash: 83ea7c1390fd3af0dbea122863f7085e2126b5a4
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/convert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/convert.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/convert.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># convert

Strumento della suite immagineMagick per la conversione di immagini.
Maggiori informazioni: <https://imagemagick.org/script/convert.php>.

- Converti un'immagine da JPEG a PNG:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>

- Scala un'immagine al 50% delle sue dimensioni originali:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>

- Scala un'immagine ad una dimensione massima di 640x480 mantenendo le proporzioni originali:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>

- Concatena più immagini orizzontalmente:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine3.png</span>` +append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine123.png</span>

- Crea una GIF da una serie di immagini con un intervallo di 100ms tra ogni immagine:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine3.png</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">animazione.gif</span>

- Crea un'immagine a tinta unita di un determinato colore:

`convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immagine.png</span>
