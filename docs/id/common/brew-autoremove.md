---
layout: page
title: common/brew-autoremove (Indonesia)
description: "Hapus formula-formula yang tak digunakan dan sebelumnya dibutuhkan untuk memasang formula lain."
content_hash: 7af429b705586049ef53eaf7bb0f40426d25fd3c
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/common/brew-autoremove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/brew-autoremove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># brew autoremove

Hapus formula-formula yang tak digunakan dan sebelumnya dibutuhkan untuk memasang formula lain.
Informasi lebih lanjut: <https://docs.brew.sh/Manpage#autoremove---dry-run>.

- Hapus semua formula yang tak digunakan kembali:

`brew autoremove`

- Tampilkan daftar formula yang dapat dihapus tanpa melakukannya (dry-run):

`brew autoremove --dry-run`
