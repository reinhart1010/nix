---
layout: page
title: common/compare (Deutsch)
description: "Zeige Unterschiede von zwei Bildern."
content_hash: d392e15a928dbe261b3b3fd74ad895669f08df57
related_topics:
  - title: English version
    url: /en/common/compare.html
    icon: bi bi-globe
---
# compare

Zeige Unterschiede von zwei Bildern.
Weitere Informationen: <https://imagemagick.org/script/compare.php>.

- Vergleiche 2 Bilder:

`compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diff.png</span>

- Vergleiche 2 Bilder mit einer bestimmten Metrik (standardmäßig NCC):

`compare -verbose -metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PSNR</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild1.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild2.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diff.png</span>
