---
layout: page
title: common/chmod (Indonesia)
description: "Mengubah hak akses pengguna suatu file atau direktori."
content_hash: 25db3d6997021abd4840ea45062d3895a43485dd
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chmod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chmod

Mengubah hak akses pengguna suatu file atau direktori.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/chmod>.

- Berikan pengguna pembuat file hak untuk mengeksekusinya (misal: sebagai script):

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Berikan hak kepada pengguna untuk membaca ([r]ead) dan menulis ([w]rite) suatu file atau direktori:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori</span>

- Hentikan hak akses terhadap [g]rup untuk mengeksekusi suatu file:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Berikan semua pengguna hak untuk membaca dan mengeksekusi suatu file:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Berikan hak-hak akses suatu file yang sama dari [g]rup kepada pengguna di luar grup ([o]thers):

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Hentikan semua hak akses suatu file:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Berikan hak tulis suatu direktori bagi [g]rup dan lainnya secara [R]ekursif (termasuk seluruh file yang terkandung di dalamnya):

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Berikan hak semua pengguna untuk membaca seluruh file dan mengeksekusi para sub-direktori dalam suatu direktori:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>
