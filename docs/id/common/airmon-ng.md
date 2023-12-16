---
layout: page
title: common/airmon-ng (Indonesia)
description: "Nyalakan mode pengawasan pada perangkat jaringan nirkabel/wireless."
content_hash: 447248a8a36789220ffa1c23963e2a7f3009b8af
last_modified_at: 2023-12-16
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
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airmon-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airmon-ng

Nyalakan mode pengawasan pada perangkat jaringan nirkabel/wireless.
Bagian dari paket perangkat lunak jaringan Aircrack-ng.
Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Tampilkan daftar perangkat nirkabel beserta statusnya:

`sudo airmon-ng`

- Mulai awasi jaringan untuk perangkat tertentu:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Hentikan proses-proses mengganggu yang memanfaatkan perangkat nirkabel:

`sudo airmon-ng check kill`

- Matikan mode pengawasan untuk interface jaringan tertentu:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
