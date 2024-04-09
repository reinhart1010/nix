---
layout: page
title: sunos/svcadm (Indonesia)
description: "Instansi untuk manipulasi hak akses layanan."
content_hash: 3b1ad6c63de18b498fb8ba3209daf069081f7157
last_modified_at: 2024-04-09
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcadm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/svcadm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># svcadm

Instansi untuk manipulasi hak akses layanan.
Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Izinkan sebuah servis yang ada dalam basis data servis:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_servis</span>

- Larang servis:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama servis</span>

- Jalankan ulang sebuah servis yang berjalan:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama servis</span>

- Perintahkan servis untuk baca ulang berkas konfigurasi:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama servis</span>

- Bersihkan sebuah servis dari kondisi perawatan dan perintahkan untuk berjalan:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama servis</span>
