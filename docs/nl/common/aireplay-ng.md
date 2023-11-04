---
layout: page
title: common/aireplay-ng (Nederlands)
description: "Injecteer pakketten in een draadloos netwerk."
content_hash: d05e34a7d148c6e76fb28afab7ca62dff1ae66dc
last_modified_at: 2023-11-04
related_topics:
  - title: বাংলা version
    url: /bn/common/aireplay-ng.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/aireplay-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aireplay-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aireplay-ng.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/aireplay-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aireplay-ng.html
    icon: bi bi-globe
---
# aireplay-ng

Injecteer pakketten in een draadloos netwerk.
Deel van `aircrack-ng`.
Meer Informatie: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Stuur een specifiek aantal losgekoppelde pakketten op basis van het MAC-adres van een toegangspunt, het MAC-adres van een cliënt en een interface:

`sudo aireplay-ng --deauth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nummer</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` --dmac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cliënt_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
