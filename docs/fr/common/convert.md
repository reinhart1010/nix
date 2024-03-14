---
layout: page
title: common/convert (français)
description: "Outil de conversion d'image d'ImageMagick."
content_hash: 46a63eda4a4761d614d45b4d3c7b4063981e4311
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/convert.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/convert.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/convert.html
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

Outil de conversion d'image d'ImageMagick.
Plus d'informations : <https://imagemagick.org/script/convert.php>.

- Convertir une image JPEG en PNG :

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>

- Redimensionner une image à 50% de ses dimensions d'origine :

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>

- Redimensionner une image en conservant son ratio hauteur/largeur initial pour une taille maximum de 640x480 :

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>

- Coller plusieurs images horizontallement :

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image3.png</span>` +append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image123.png</span>

- Coller plusieurs images verticalement :

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image3.png</span>` -append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image123.png</span>

- Créer un gif à partir d'une série d'images avec un délai de 100ms entre chaque :

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image3.png</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">animation.gif</span>

- Créer une image avec un simple arrière-plan uni :

`convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.png</span>
