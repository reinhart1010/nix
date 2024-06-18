---
layout: page
title: common/arp-scan (Indonesia)
description: "Kirim paket ARP menuju kumpulan alamat IP atau host untuk memindai suatu jaringan komputer lokal."
content_hash: c8f1d08c06d69c1e5c2d11f5c4f18b3bf6278e14
last_modified_at: 2024-06-18
related_topics:
  - title: Deutsch version
    url: /de/common/arp-scan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/arp-scan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arp-scan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/arp-scan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arp-scan.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/arp-scan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/arp-scan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># arp-scan

Kirim paket ARP menuju kumpulan alamat IP atau host untuk memindai suatu jaringan komputer lokal.
Informasi lebih lanjut: <https://github.com/royhills/arp-scan>.

- Pindai jaringan lokal yang terhubung saat ini:

`arp-scan --localnet`

- Pindai suatu alamat IP dengan pengaturan bitmask khusus:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.1.1</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">24</span>

- Pindai suatu jaringan IP menggunakan rentang alamat tertentu:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">172.0.0.0</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.31</span>

- Pindai suatu jaringan IP menggunakan net mask khusus:

`arp-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10.0.0.0</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">255.255.255.0</span>
