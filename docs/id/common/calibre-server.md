---
layout: page
title: common/calibre-server (Indonesia)
description: "Suatu aplikasi peladen (server) untuk membagikan buku digital (e-book) dalam jaringan."
content_hash: 8e0384897fa2124fc86fee1bbe90144430609319
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/calibre-server.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/calibre-server.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibre-server.html
    icon: bi bi-globe
tldri18n_status: 2
---
# calibre-server

Suatu aplikasi peladen (server) untuk membagikan buku digital (e-book) dalam jaringan.
Catatan: buku-buku digital harus sebelumnya diimpor menuju perpustakaan baik melalui aplikasi GUI maupun perintah `calibredb`.
Bagian dari aplikasi perpustakaan buku digital Calibre.
Informasi lebih lanjut: <https://manual.calibre-ebook.com/generated/en/calibre-server.html>.

- Jalankan peladen untuk berbagi buku digital. Akses perpustakaan pada <http://localhost:8080>:

`calibre-server`

- Jalankan peladen pada port berbeda. Akses perpustakaan pada <http://localhost:port>:

`calibre-server --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Lindungi peladen dengan membutuhkan kata sandi (password) untuk mengaksesnya:

`calibre-server --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>
