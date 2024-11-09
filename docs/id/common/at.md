---
layout: page
title: common/at (Indonesia)
description: "Jalankan kumpulan perintah pada lain waktu."
content_hash: af4f7ee6c4b964617166a68210c81cdb547e05eb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/at.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># at

Jalankan kumpulan perintah pada lain waktu.
Hasil penugasan perintah akan dikirimkan menuju surel pengguna.
Informasi lebih lanjut: <https://manned.org/at>.

- Jalankan piranti daemon `atd`:

`systemctl start atd`

- Buat perintah secara interaktif untuk dijalankan dalam 5 menit ke depan (gunakan `<Ctrl> + D` jika selesai menulis):

`at now + 5 minutes`

- Buat perintah secara interaktif dan jalankan pada waktu tertentu:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Jalankan perintah yang dimasukkan ke dalam `stdin` pada hari ini pukul 10.00 pagi:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`" | at 1000`

- Jalankan perintah yang diatur dalam suatu berkas pada hari Selasa berikutnya:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` 9:30 PM Tue`
