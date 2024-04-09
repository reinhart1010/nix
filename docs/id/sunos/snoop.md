---
layout: page
title: sunos/snoop (Indonesia)
description: "Pengendus paket jaringan."
content_hash: 13064f35d48ab88edeb092091c25d0e1ce0e2bec
last_modified_at: 2024-04-09
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/snoop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># snoop

Pengendus paket jaringan.
tcpdump untuk SunOS.
Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Tangkap paket pada antarmuka jaringan tertentu:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- Simpan paket yang tertangkap pada sebuah berkas dari pada menampilkannya:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan rangkuman lapisan protokol paket-paket dari sebuah berkas dengan rinci:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalur/ke/berkas</span>

- Tangkap paket jaringan yang datang dari sebuah nama host dan pergi ke port yang ditentukan:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_host</span>

- Tangkap dan tampilkan sebuah hex-dump dari pertukaran paket jaringan di antara 2 alamat IP:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip2</span>
