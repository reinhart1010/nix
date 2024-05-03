---
layout: page
title: common/airodump-ng (Indonesia)
description: "Tangkap para paket dan tampilkan informasi mengenai jaringan nirkabel/wireless."
content_hash: a64e2a42d19c558145b6ef488df03c6ec6252521
last_modified_at: 2024-05-03
related_topics:
  - title: Deutsch version
    url: /de/common/airodump-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airodump-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airodump-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airodump-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airodump-ng.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airodump-ng

Tangkap para paket dan tampilkan informasi mengenai jaringan nirkabel/wireless.
Bagian dari paket perangkat lunak jaringan Aircrack-ng.
Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Tangkap para paket dan tampilkan daftar jaringan nirkabel dalam frekuensi 2.4GHz:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Tangkap para paket dan tampilkan daftar jaringan nirkabel dalam frekuensi 5GHz:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` --band a`

- Tangkap para paket dan tampilkan daftar jaringan nirkabel, baik dalam frekuensi 2.4GHz maupun 5GHz:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>` --band abg`

- Tangkap para paket dan tampilkan informasi jaringan nirkabel berdasarkan alamat MAC dan kanal jaringan, kemudian simpan hasil ke dalam suatu file:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
