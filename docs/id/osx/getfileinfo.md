---
layout: page
title: osx/getfileinfo (Indonesia)
description: "Dapatkan informasi sebuah file dalam direktori yang terkandung dalam penyimpanan berbasis HFS+."
content_hash: e283cc401b0b5a5692291ce663322a98fdd93e46
last_modified_at: 2023-12-02
related_topics:
  - title: English version
    url: /en/osx/getfileinfo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/getfileinfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/getfileinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/getfileinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># GetFileInfo

Dapatkan informasi sebuah file dalam direktori yang terkandung dalam penyimpanan berbasis HFS+.
Informasi lebih lanjut: <https://www.unix.com/man-page/osx/1/GetFileInfo/>.

- Tampilkan informasi mengenai suatu file:

`GetFileInfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Tampilkan tanggal dan waktu saat file tersebut pertama kali [d]ibuat:

`GetFileInfo -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Tampilkan tanggal dan waktu saat file tersebut terakhir kali di[m]odifikasi:

`GetFileInfo -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Tampilkan nama pengguna yang men[c]iptakan file tersebut:

`GetFileInfo -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>
