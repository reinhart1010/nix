---
layout: page
title: common/echo (Indonesia)
description: "Cetak ulang argumen-argumen yang dimasukkan ke dalam layar perangkat."
content_hash: 2c4c1da86c10335a8771fe94bb7e72b79b3c9c8b
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/echo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/echo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/echo.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/echo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/echo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/echo.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/echo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/echo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/echo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/echo.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/echo.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/common/echo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/echo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/echo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# echo

Cetak ulang argumen-argumen yang dimasukkan ke dalam layar perangkat.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Cetak sebuah pesan teks. Catatan: penggunaan tanda petik bersifat opsional:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Halo Dunia</span>`"`

- Cetak sebuah pesan bersama suatu variabel lingkungan (environment variable):

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Variabel path saya adalah $PATH</span>`"`

- Cetak sebuah pesan tanpa mencetak baris teks baru (tanpa [n]ewline):

`echo -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Halo Dunia</span>`"`

- Tambahkan isi pesan ke dalam suatu berkas teks:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Halo Dunia</span>`" >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas.txt</span>

- Aktifkan fitur interpretasi penggunaan tanda garis miring terbalik sebagai penanda karakter khusus:

`echo -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Kolom 1\tKolom 2</span>`"`

- Cetak status keluar dari perintah terakhir yang dieksekusi (Catatan: Dalam Windows Command Prompt dan PowerShell, perintah yang setara adalah `echo %errorlevel%` dan `$lastexitcode`):

`echo $?`
