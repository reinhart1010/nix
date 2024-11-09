---
layout: page
title: common/assimp (Indonesia)
description: "Klien baris perintah untuk pustaka Open Asset Import Library."
content_hash: 46e09d3ef8de5cfa09569d0f9ca7939244433c55
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/assimp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/assimp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/assimp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/assimp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/assimp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/assimp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># assimp

Klien baris perintah untuk pustaka Open Asset Import Library.
Mendukung pemuatan 40+ format file 3D, dan mengekspor ke beberapa format 3D populer.
Informasi lebih lanjut: <https://assimp-docs.readthedocs.io/>.

- Tampilkan daftar format berkas impor yang didukung:

`assimp listext`

- Tampilkan daftar format berkas ekspor yang didukung:

`assimp listexport`

- Ubah isi suatu berkas menuju salah satu dari format berkas ekspor/luaran yang didukung, menggunakan daftar parameter bawaan:

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_masukan.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_luaran.obj</span>

- Ubah isi suatu berkas menggunakan kumpulan parameter kustom (daftar parameter yang tersedia dapat dilihat pada berkas dox_cmd.h pada kode sumber assimp):

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_masukan.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_luaran.obj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kumpulan_parameter</span>

- Tampilkan ringkasan isi suatu berkas objek 3D:

`assimp info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan bantuan:

`assimp help`

- Tampilkan bantuan atas suatu subperintah:

`assimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subperintah</span>` --help`
