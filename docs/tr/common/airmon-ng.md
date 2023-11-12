---
layout: page
title: common/airmon-ng (Türkçe)
description: "Kablosuz ağ cihazlarında izleme modunu etkinleştirin."
content_hash: 7654c25a7d564242bc8bcfce869194f9a675e716
last_modified_at: 2023-11-12
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
  - title: Nederlands version
    url: /nl/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airmon-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airmon-ng

Kablosuz ağ cihazlarında izleme modunu etkinleştirin.
Daha fazla bilgi için: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Kablosuz cihazları ve durumlarını listeleyin:

`sudo airmon-ng`

- Belirli bir cihaz için izleme modunu açın:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Kablosuz cihazları kullanan rahatsız edici işlemleri sonlandırın:

`sudo airmon-ng check kill`

- Belirli bir ağ arabirimi için izleme modunu kapatın:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
