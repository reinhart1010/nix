---
layout: page
title: common/frpc (Indonesia)
description: "Hubungkan perangkat menuju jaringan proksi yang diatur oleh suatu peladen/server `frps`."
content_hash: bad66fc740fb9b80c47373e9953cea1c58df0da7
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/frpc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/frpc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/frpc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/frpc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># frpc

Hubungkan perangkat menuju jaringan proksi yang diatur oleh suatu peladen/server `frps`.
Bagian dari `frp`.
Informasi lebih lanjut: <https://github.com/fatedier/frp>.

- Jalankan layanan klien, menggunakan berkas konfigurasi bawaan/default (diasumsikan merupakan berkas `frps.ini` yang terletak pada direktori saat ini):

`frpc`

- Jalankan layanan menggunakan berkas konfigurasi dengan format terbaru berbasis TOML (`frps.toml` daripada `frps.ini`) pada direktori saat ini:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Start the service, using a specific configuration file:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Periksa apakah isi suatu berkas konfigurasi menggunakan format yang valid:

`frpc verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan isi skrip shell yang perlu dijalankan untuk mengaktifkan fitur penyelesaian perintah otomatis (autocomplete) bagi Bash, fish, PowerShell, maupun Zsh:

`frpc completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Tampilkan informasi versi:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
