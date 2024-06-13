---
layout: page
title: common/brew-bundle (Indonesia)
description: "Pembungkus untuk Homebrew, Homebrew Cask, dan App Store untuk macOS."
content_hash: 2f554aac07ef587985ea6afa0cb184af284618e3
last_modified_at: 2024-06-13
related_topics:
  - title: Deutsch version
    url: /de/common/brew-bundle.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/brew-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew-bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew-bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew bundle

Pembungkus untuk Homebrew, Homebrew Cask, dan App Store untuk macOS.
Informasi lebih lanjut: <https://github.com/Homebrew/homebrew-bundle>.

- Pasang seluruh paket menurut data Brewfile pada direktori saat ini:

`brew bundle`

- Pasang seluruh paket menurut data Brewfile pada lokasi tertentu:

`brew bundle --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Buat suatu berkas Brewfile berisikan daftar seluruh paket yang terpasang saat ini:

`brew bundle dump`

- Hapus seluruh formula yang tidak didefinisikan atau dibutuhkan pada formula dalam berkas Brewfile:

`brew bundle cleanup --force`

- Cari tahu apakah terdapat formula yang perlu dipasang atau dimutakhirkan dalam berkas Brewfile:

`brew bundle check`

- Tampilkan seluruh entri dalam berkas Brewfile:

`brew bundle list --all`
