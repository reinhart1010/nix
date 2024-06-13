---
layout: page
title: common/brew-install (Indonesia)
description: "Pasang suatu formula atau cask pada Homebrew."
content_hash: 7c4b787a305ec9c372a15ad3c95cbcd60621f29d
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/brew-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew install

Pasang suatu formula atau cask pada Homebrew.
Informasi lebih lanjut: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- Pasang suatu formula/cask:

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>

- Bangun dan pasang suatu formula dari kode sumber (seluruh formula yang dibutuhkan tetap akan diunduh sebagai berkas jadian / bottle):

`brew install --build-from-source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Unduh manifest dan tampilkan daftar formula/cask yang akan dipasang tanpa melakukannya (dry-run):

`brew install --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula|cask</span>
