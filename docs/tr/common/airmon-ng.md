---
layout: page
title: common/airmon-ng (Türkçe)
description: "Kablosuz ağ cihazlarında izleme modunu etkinleştirin."
content_hash: 60453d957e451e84a42c0b8175733121f5c7f899
related_topics:
  - title: English version
    url: /en/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
---
# airmon-ng

Kablosuz ağ cihazlarında izleme modunu etkinleştirin.
Daha fazla bilgi: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Kablosuz cihazları ve durumlarını listeleyin:

`sudo airmon-ng`

- Belirli bir cihaz için izleme modunu açın:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Kablosuz cihazları kullanan rahatsız edici işlemleri sonlandırın:

`sudo airmon-ng check kill`

- Belirli bir ağ arabirimi için izleme modunu kapatın:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
