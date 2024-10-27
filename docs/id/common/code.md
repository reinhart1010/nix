---
layout: page
title: common/code (Indonesia)
description: "Pengolah kode komputer yang tersedia lintas platform dan dapat diperluas."
content_hash: 65b690b53f11c71eeccc7bc015f825b193775a48
last_modified_at: 2024-10-27
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/code.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/code.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/code.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
tldri18n_status: 2
---
# code

Pengolah kode komputer yang tersedia lintas platform dan dapat diperluas.
Informasi lebih lanjut: <https://github.com/microsoft/vscode>.

- Jalankan aplikasi Visual Studio Code:

`code`

- Buka kumpulan berkas atau direktori ke dalam program pengolah:

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...</span>

- Bandingkan isi antara dua berkas teks:

`code --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas2</span>

- Buka kumpulan berkas atau direktori menuju sebuah jendela pengolah baru:

`code --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...</span>

- Pasang/bongkat suatu paket ekstensi:

`code --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>`-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">penerbit.ekstensi</span>

- Tampilkan daftar ekstensi yang terpasang:

`code --list-extensions`

- Tampilkan daftar ekstensi terpasang beserta versi masing-masing ekstensi:

`code --list-extensions --show-versions`

- Jalankan program pengolah sebagai superuser (root) dengan menyimpan data aplikasi ke dalam suatu direktori:

`sudo code --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>
