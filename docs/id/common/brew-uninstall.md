---
layout: page
title: common/brew-uninstall (Indonesia)
description: "Bongkar pemasangan suatu paket formula/cask Homebrew."
content_hash: d64272b2c6d4c63b6d24b74c24b1ebc787d46318
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/brew-uninstall.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew-uninstall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew uninstall

Bongkar pemasangan suatu paket formula/cask Homebrew.
Gunakan `brew autoremove` untuk menghapus kumpulan paket dependensi yang tidak dibutuhkan kembali.
Informasi lebih lanjut: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->.

- Bongkar pemasangan suatu formula/cask:

`brew uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- Bongkar pemasangan suatu cask dan hapus seluruh berkas terkait:

`brew uninstall --zap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask</span>
