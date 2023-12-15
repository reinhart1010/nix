---
layout: page
title: common/aircrack-ng (Indonesia)
description: "Retas dan dapatkan kunci WEP dan WPA/WPA2 dari proses handshake dalam paket jaringan yang ditangkap."
content_hash: 4aa77c4b4eaee6cde3c2d6c230c815456e50f274
last_modified_at: 2023-12-15
related_topics:
  - title: Deutsch version
    url: /de/common/aircrack-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aircrack-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aircrack-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aircrack-ng.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aircrack-ng.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aircrack-ng

Retas dan dapatkan kunci WEP dan WPA/WPA2 dari proses handshake dalam paket jaringan yang ditangkap.
Bagian dari paket perangkat lunak jaringan Aircrack-ng.
Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Retas dan dapatkan kunci dari file tangkapan jaringan dan file daftar kata sandi ([w]ordlist):

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/wordlist.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>

- Retas dan dapatkan kunci dari file tangkapan jaringan, [w]ordlist, dan [e]ssid milik perangkat titik akses Wi-Fi:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/wordlist.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>

- Retas dan dapatkan kunci dari file tangkapan jaringan, [w]ordlist, dan alamat MAC milik perangkat titik akses Wi-Fi:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/wordlist.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tangkapan_jaringan.cap</span>
