---
layout: page
title: common/magick-compare (Nederlands)
description: "Maak een vergelijkingsafbeelding om visueel de verschillen te zien tussen twee afbeeldingen."
content_hash: 3c1bc934af4356d9566a2a7f746d02f26ff29b69
last_modified_at: 2024-06-09
related_topics:
  - title: Deutsch version
    url: /de/common/magick-compare.html
    icon: bi bi-globe
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

Maak een vergelijkingsafbeelding om visueel de verschillen te zien tussen twee afbeeldingen.
Bekijk ook: `magick`.
Meer informatie: <https://imagemagick.org/script/compare.php>.

- Vergelijk twee afbeeldingen:

`magick compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/diff.png</span>

- Vergelijk twee afbeelding door gebruik te maken van de gespecificeerde metriek:

`magick compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/diff.png</span>
