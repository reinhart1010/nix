---
layout: page
title: common/airdecap-ng (Indonesia)
description: "Dekripsi file tangkapan jaringan terenkripsi dengan kunci sandi WEP, WPA, atau WPA2."
content_hash: a39a6e3e6b514ceae5c93dd974081d6687e2342b
last_modified_at: 2023-12-16
related_topics:
  - title: English version
    url: /en/common/airdecap-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airdecap-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airdecap-ng

Dekripsi file tangkapan jaringan terenkripsi dengan kunci sandi WEP, WPA, atau WPA2.
Bagian dari paket perangkat lunak jaringan Aircrack-ng.
Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- Buang informasi header jaringan wireless/nirkabel dari file tangkapan jaringan (bebas enkripsi WEP/WPA/WPA2), dan gunakan alamat MAC titik akses Wi-Fi untuk menyaringnya:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>

- Buka enkripsi WEP dari file tangkapan jaringan menggunakan kunci WEP dalam format heksadesimal:

`airdecap-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kunci_heksadesimal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>

- Buka enkripsi WPA/WPA2 dari file tangkapan jaringan menggunakan [e]ssid titik akses Wi-Fi dan kata sandi ([p]assword):

`airdecap-ng -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>

- Buka enkripsi WPA/WPA2 dari file tangkapan jaringan menggunakan [e]ssid dan kata sandi ([p]assword), tanpa menghilangkan informasi header jaringan:

`airdecap-ng -l -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>

- Buka enkripsi WPA/WPA2 dari file tangkapan jaringan menggunakan [e]ssid dan kata sandi ([p]assword), dan saring menurut alamat MAC titik akses Wi-Fi:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_mac</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>
