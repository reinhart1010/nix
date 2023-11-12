---
layout: page
title: common/convert (Deutsch)
description: "ImageMagick Bildkonvertierungswerkzeug."
content_hash: e5c7d526f964df67480afa673da7ff15cc0f862c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/convert.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/convert.html
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
tldri18n_status: 2
---
# convert

ImageMagick Bildkonvertierungswerkzeug.
Weitere Informationen: <https://imagemagick.org/script/convert.php>.

- Konvertiere ein Bild von JPG nach PNG:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.png</span>

- Skaliere ein Bild auf 50% seiner Originalgröße:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.png</span>` -resize 50% `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>

- Skaliere ein Bild unter Beibehaltung des ursprünglichen Seitenverhältnisses auf eine maximale Größe von 640x480:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.png</span>` -resize 640x480 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>

- Hänge Bilder horizontal aneinander:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild3.png</span>` +append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild123.png</span>

- Hänge Bilder vertikal aneinander:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild3.png</span>` -append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild123.png</span>

- Erstelle ein animiertes GIF aus einer Serie von Bildern mit einer Verzögerung von 100 ms zwischen den Bildern:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild3.png</span>` -delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/animation.gif</span>

- Erstelle ein Bild mit nichts als einem festen Hintergrund:

`convert -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">800x600</span>` "xc:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#ff0000</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.png</span>

- Erstelle ein Favicon aus mehreren Bildern verschiedener Größe:

`convert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild3.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.ico</span>
