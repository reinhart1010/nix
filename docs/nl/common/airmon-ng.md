---
layout: page
title: common/airmon-ng (Nederlands)
description: "Activeer de monitormodus op draadloze netwerkapparaten."
content_hash: 4049c4b43fb8213db7ad578b14a458e2388504c4
last_modified_at: 2023-07-28
related_topics:
  - title: Deutsch version
    url: /de/common/airmon-ng.html
    icon: bi bi-globe
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

Activeer de monitormodus op draadloze netwerkapparaten.
Deel van `aircrack-ng`.
Meer informatie: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Maak een lijst van draadloze apparaten en hun statussen:

`sudo airmon-ng`

- Schakel de monitormodus in voor een specifiek apparaat:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Dood storende processen die draadloze apparaten gebruiken:

`sudo airmon-ng check kill`

- Schakel de monitormodus uit voor een specifieke netwerkinterface:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
