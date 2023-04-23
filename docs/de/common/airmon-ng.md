---
layout: page
title: common/airmon-ng (Deutsch)
description: "Aktiveren des Überwachungsmodus auf Wireless Network Geräten."
content_hash: 079f5a447b7f1e1de4a180d474358be7f82b2fbb
last_modified_at: 2023-04-23
related_topics:
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airmon-ng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airmon-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airmon-ng

Aktiveren des Überwachungsmodus auf Wireless Network Geräten.
Teil von `aircrack-ng`.
Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Liste Wireless Geräte und deren Status auf:

`sudo airmon-ng`

- Aktiviere den Überwachungsmodus für ein bestimmtes Gerät:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Kille störende Prozesse, die das Wireless Gerät verwenden:

`sudo airmon-ng check kill`

- Deaktiviere den Überwachungsmodus für ein spezifisches Interface:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
