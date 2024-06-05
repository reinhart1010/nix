---
layout: page
title: common/magick-compare (Deutsch)
description: "Zeige Unterschiede von zwei Bildern."
content_hash: 0837bead05cb86228f5c766353955bf7c7677950
last_modified_at: 2024-06-05
related_topics:
  - title: English version
    url: /en/common/magick-compare.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/magick-compare.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/magick-compare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# magick compare

Zeige Unterschiede von zwei Bildern.
Weitere Informationen: <https://imagemagick.org/script/compare.php>.

- Vergleiche 2 Bilder:

`magick compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diff.png</span>

- Vergleiche 2 Bilder mit einer bestimmten Metrik (standardmäßig NCC):

`magick compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diff.png</span>
