---
layout: page
title: common/brew (Indonesia)
description: "Homebrew - suatu manajer paket bagi macOS dan Linux."
content_hash: 17b6a4a0364bffb01aee940848065f1eaca3dc78
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew

Homebrew - suatu manajer paket bagi macOS dan Linux.
Beberapa subperintah seperti `install` mempunyai dokumentasi terpisah.
Informasi lebih lanjut: <https://docs.brew.sh/Manpage>.

- Pasang versi terkini oleh suatu formula atau cask (gunakan `--devel` untuk memasang versi pengembangan):

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Tampilkan daftar formula dan cask yang terpasang:

`brew list`

- Mutakhirkan suatu formula atau cask (jika nama tidak disediakan, semua formula dan cask terpasang akan dimutakhirkan):

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Dapatkan program Homebrew versi terkini dan semua formula dan cask yang tersedia dari repositori paket Homebrew:

`brew update`

- Tampilkan daftar formula dan cask yang memiliki versi lebih baru dari yang terpasang:

`brew outdated`

- Cari formula (paket biasa) serta cask (berkas aplikasi `.app` bagi macOS):

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks</span>

- Tampilkan informasi mengenai suatu formula atau cask (versi, lokasi pemasangan, formula/cask tambahan yang dibutuhkan, dll.):

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Cek kondisi pemasangan Homebrew saat ini untuk mendeteksi kemungkinan galat atau masalah:

`brew doctor`
