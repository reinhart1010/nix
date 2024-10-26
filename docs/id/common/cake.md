---
layout: page
title: common/cake (Indonesia)
description: "Alat baris perintah untuk memproses proyek aplikasi web berbasis framework CakePHP."
content_hash: 3b5b601c019a0c54d87f9a509d312d45e837ca6a
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/cake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cake.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cake.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cake

Alat baris perintah untuk memproses proyek aplikasi web berbasis framework CakePHP.
Informasi lebih lanjut: <https://cakephp.org>.

- Tampilkan informasi dasar mengenai proyek aplikasi saat ini beserta daftar perintah:

`cake`

- Tampilkan daftar rute aplikasi web yang tersedia:

`cake routes`

- Hapus berkas-berkas cache konfigurasi proyek:

`cake cache clear_all`

- Bangun berkas cache metadata bagi proyek saat ini:

`cake schema_cache build --connection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">koneksi</span>

- Hapus berkas cache metadata:

`cake schema_cache clear`

- Hapus suatu tabel cache:

`cake schema_cache clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_tabel</span>

- Jalankan sebuah peladen web untuk kepentingan pengembangan (secara bawaan mengarah menuju port 8765):

`cake server`

- Jalankan sebuah proses REPL (syel interaktif):

`cake console`
