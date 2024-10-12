---
layout: page
title: common/frps (Indonesia)
description: "Buat suatu peladen pelayan jaringan proksi terbalik (reverse proksi)."
content_hash: cd952e7acc078cc41b37cdff23b54fd05df938fd
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/frps.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/frps.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/frps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# frps

Buat suatu peladen pelayan jaringan proksi terbalik (reverse proksi).
Bagian dari `frp`.
Informasi lebih lanjut: <https://github.com/fatedier/frp>.

- Jalankan layanan peladen, menggunakan berkas konfigurasi bawaan/default (diasumsikan merupakan berkas `frps.ini` yang terletak pada direktori saat ini):

`frps`

- Jalankan layanan menggunakan berkas konfigurasi dengan format terbaru berbasis TOML (`frps.toml` daripada `frps.ini`) pada direktori saat ini:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Start the service, using a specific configuration file:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Periksa apakah isi suatu berkas konfigurasi menggunakan format yang valid:

`frps verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan isi skrip shell yang perlu dijalankan untuk mengaktifkan fitur penyelesaian perintah otomatis (autocomplete) bagi Bash, fish, PowerShell, maupun Zsh:

`frps completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Tampilkan informasi versi:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
