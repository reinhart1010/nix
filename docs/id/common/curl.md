---
layout: page
title: common/curl (Indonesia)
description: "Mentransfer data dari atau ke server."
content_hash: 7014b8eb30e2ca99b73d9cc8d06f031c294aa767
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/curl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/curl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/curl.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/curl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/curl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/curl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/curl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/curl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# curl

Mentransfer data dari atau ke server.
Mendukung sebagian besar protokol, termasuk HTTP, FTP, dan POP3.
Informasi lebih lanjut: <https://curl.se/docs/manpage.html>.

- Unduh konten URL ke file:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namafile</span>

- Unduh file, simpan hasilnya dengan nama file yang ditentukan oleh URL:

`curl --remote-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com/namafile</span>

- Unduh file, mengikuti pengalihan lokasi, dan secara otomatis melanjutkan transfer file sebelumnya:

`curl --fail --remote-name --location --continue-at - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com/filename</span>

- Mengirim data form yang telah di encode (permintaan POST atau tipe data `application/x-www-form-urlencoded`). Gunakan `--data @file_name` atau `--data @'-'` untuk membaca dari STDIN:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'name=bob'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com/form</span>

- Mengirim sebuah permintaan dengan header tambahan, menggunakan metode HTTP kustom:

`curl --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'X-My-Header: 123'</span>` --request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com</span>

- Mengirim data dalam format JSON, Menentukan jenis konten yang sesuai header:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Content-Type: application/json'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com/users/1234</span>

- Memberikan nama pengguna dan kata sandi untuk otentikasi server:

`curl --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com</span>

- Memberikan sertifikat klien dan kunci untuk sumber daya, melewati validasi sertifikat:

`curl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://contoh.com</span>
