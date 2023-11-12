---
layout: page
title: windows/choco-install (Indonesia)
description: "Instal satu paket atau lebih dengan Chocolatey."
content_hash: 8bbbc3e6fbb6a742ea8dac635052a80116762e3d
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-install.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco install

Instal satu paket atau lebih dengan Chocolatey.
Informasi lebih lanjut: <https://chocolatey.org/docs/commands-install>.

- Instal satu paket atau lebih paket yang dipisahkan oleh spasi:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Instal paket dari file konfigurasi khusus:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/paket.config</span>

- Instal file nuspec atau nupkg tertentu:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Instal versi paket tertentu:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Izinkan menginstal beberapa versi paket:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --allow-multiple`

- Konfirmasikan semua prompt secara otomatis:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --yes`

- Tentukan sumber khusus untuk menerima paket:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_sumber|alias</span>

- Berikan nama pengguna dan kata sandi untuk otentikasi:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>
