---
layout: page
title: common/airmon-ng (français)
description: "Active le mode surveillance sur les appareils sans fils."
content_hash: 0fa85276d3996648e1db27a376c87979a731e90f
related_topics:
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airmon-ng

Active le mode surveillance sur les appareils sans fils.
Plus d'informations : <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Liste les appareils sans fils et leurs statuts :

`sudo airmon-ng`

- Allume le mode surveillance sur un appareil spécifique :

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Tue les processus nuisibles qui utilisent les appareils sans fils :

`sudo airmon-ng check kill`

- Éteint le mode surveillance pour une interface réseau spécifique :

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
