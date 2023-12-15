---
layout: page
title: common/adguardhome (Indonesia)
description: "Perangkat lunak untuk memblokir iklan dan upaya pelacakan dalam jaringan internet."
content_hash: 2f4fbced98255c48ab7275bea8b8b00e5a9bdb52
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/adguardhome.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adguardhome.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/adguardhome.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/adguardhome.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adguardhome.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/adguardhome.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># AdGuardHome

Perangkat lunak untuk memblokir iklan dan upaya pelacakan dalam jaringan internet.
Informasi lebih lanjut: <https://github.com/AdguardTeam/AdGuardHome>.

- Jalankan AdGuard Home:

`AdGuardHome`

- Jalankan AdGuard Home dengan konfigurasi tertentu:

`AdGuardHome --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/AdGuardHome.yaml</span>

- Tentukan direktori penyimpanan data untuk AdGuard Home:

`AdGuardHome --work-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Pasang atau bongkar AdGuard Home sebagai layanan/daemon sistem operasi:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>

- Jalankan AdGuard Home sebagai layanan/daemon:

`AdGuardHome --service start`

- Muat ulang konfigurasi layanan AdGuard Home:

`AdGuardHome --service reload`

- Matikan atau nyalakan ulang layanan AdGuard Home:

`AdGuardHome --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stop|restart</span>
