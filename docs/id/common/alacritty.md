---
layout: page
title: common/alacritty (Indonesia)
description: "Lintas platform, terakselerasi GPU terminal emulator."
content_hash: ad9c6f241a36d8bf814171dcc0a2374bebb4143b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alacritty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alacritty.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alacritty.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alacritty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alacritty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alacritty.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alacritty.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alacritty

Lintas platform, terakselerasi GPU terminal emulator.
Informasi lebih lanjut: <https://github.com/alacritty/alacritty>.

- Membuka jendela Alacritty baru:

`alacritty`

- Menjalankan Alacritty pada direktori tertentu:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/direktori</span>

- Menjalankan perintah di jendela Alacritty baru:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Menentukan berkas konfigurasi alternatif (nilai default `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/konfigurasi.yml</span>

- Menjalankan dengan mengaktifkan pemuatan ulang konfigurasi secara langsung/otomatis (dapat juga diaktifkan secara default di `alacritty.yml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/konfigurasi.yml</span>
