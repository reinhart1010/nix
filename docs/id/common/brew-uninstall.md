---
layout: page
title: common/brew-uninstall (Indonesia)
description: "Bongkar pemasangan suatu paket formula/cask Homebrew."
content_hash: d64272b2c6d4c63b6d24b74c24b1ebc787d46318
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/brew-uninstall.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew-uninstall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-uninstall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew uninstall

Bongkar pemasangan suatu paket formula/cask Homebrew.
Gunakan `brew autoremove` untuk menghapus kumpulan paket dependensi yang tidak dibutuhkan kembali.
Informasi lebih lanjut: <https://docs.brew.sh/Manpage#uninstall-remove-rm-options-installed_formulainstalled_cask->.

- Bongkar pemasangan suatu formula/cask:

`brew uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- Bongkar pemasangan suatu cask dan hapus seluruh berkas terkait:

`brew uninstall --zap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cask</span>
