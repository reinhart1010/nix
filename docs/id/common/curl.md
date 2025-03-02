---
layout: page
title: common/curl (Indonesia)
description: "Mentransfer data dari atau menuju suatu server."
content_hash: 6c4da0f414b265eceb95ea280b68ce0cdd80a0a8
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/curl.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/curl.html
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
  - title: Nederlands version
    url: /nl/common/curl.html
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

Mentransfer data dari atau menuju suatu server.
Mendukung sebagian besar protokol, termasuk HTTP, FTP, dan POP3.
Informasi lebih lanjut: <https://curl.se/docs/manpage.html>.

- Buat suatu permintaan HTTP GET dan tampilkan respons menuju `stdout`:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Buat suatu permintaan HTTP GET, ikuti (fo[L]low) seluruh permintaan redirect `3xx`, dan tampilkan ([D]ump) seluruh data header beserta isi respons menuju `stdout`:

`curl --location --dump-header - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Unduh dan simpan suatu berkas dengan nama berkas yang ditentukan oleh URL:

`curl --remote-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://contoh.com/nama_berkas.zip</span>

- Kirim suatu [d]ata dengan format form-encoded (permintaan POST dengan format data `application/x-www-form-urlencoded`). Gunakan `--data @file_name` atau `--data @'-'` untuk membaca dari `stdin`:

`curl -X POST --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'name=bob'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/form</span>

- Kirim sebuah permintaan dengan suatu informasi header ekstra, menggunakan metode HTTP kustom yang dikirimkan menggunakan suatu pro[x]i (seperti BurpSuite), mengabaikan peringatan sertifikat TLS yang ditandatangani secara mandiri (self-signed):

`curl -k --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Authorization: Bearer token'</span>` --request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|PUT|POST|DELETE|PATCH|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Kirim data dalam format JSON, dengan menetapkan isi HTTP [H]eader Content-Type:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Content-Type: application/json'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/pengguna/1234</span>

- Gunakan suatu sertifikat klien dan berkas kunci dalam mengenkripsi permintaan HTTP, dengan mengabaikan proses validasi sertifikat TLS:

`curl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sertifikat_klien.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kunci.pem</span>` --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Ubah nama host menjadi alamat IP khusus, dengan keluaran [v]erbose (mirip dengan menyunting berkas `/etc/hosts` untuk resolusi DNS khusus):

`curl --verbose --resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
