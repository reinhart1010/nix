---
layout: page
title: common/rm (Indonesia)
description: "Menghapus berkas atau direktori."
content_hash: fa3f7110a410cb2e7616586274e4c451df14f5a0
related_topics:
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
---
# rm

Menghapus berkas atau direktori.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/rm>.

- Menghapus berkas dari lokasi manapun:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/berkas/lainnya</span>

- Menghapus direktori dan semua subdirektorinya secara rekursif:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/direktori</span>

- Menghapus direktori secara paksa, tanpa meminta konfirmasi atau menampilkan pesan kesalahan:

`rm -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/direktori</span>

- Menghapus banyak berkas secara interaktif, dengan meminta konfirmasi sebelum setiap penghapusan:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(beberapa)_berkas</span>

- Menghapus berkas dengan mode verbose, mencetak pesan untuk setiap berkas yang terhapus:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/directori/*</span>
