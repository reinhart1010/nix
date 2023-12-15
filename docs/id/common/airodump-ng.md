---
layout: page
title: common/airodump-ng (Indonesia)
description: "Tangkap para paket dan tampilkan informasi mengenai jaringan nirkabel/wireless."
content_hash: e4f4efd0349e4f2380f89264d85550f70ca4f95b
last_modified_at: 2023-12-15
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/airodump-ng.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># airodump-ng

Tangkap para paket dan tampilkan informasi mengenai jaringan nirkabel/wireless.
Bagian dari paket perangkat lunak jaringan Aircrack-ng.
Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Tangkap para paket dan tampilkan informasi jaringan nirkabel tertentu:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>

- Tangkap para paket dan tampilkan informasi jaringan nirkabel berdasarkan alamat MAC dan kanal jaringan, kemudian simpan hasil ke dalam suatu file:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
