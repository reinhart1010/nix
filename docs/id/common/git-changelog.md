---
layout: page
title: common/git-changelog (Indonesia)
description: "Buat laporan riwayat perubahan (changelog) dari daftar komit dan tag yang terkandung dalam repositori Git."
content_hash: 2d8f2e360859ddbfef4868f54ae9a98a5d58f548
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-changelog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git changelog

Buat laporan riwayat perubahan (changelog) dari daftar komit dan tag yang terkandung dalam repositori Git.
Bagian dari `git-extras`:
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-changelog>.

- Buat atau mutakhirkan file `History.md` berisikan riwayat komit sejak tag komit Git terkini:

`git changelog`

- Tampilkan daftar komit pada versi saat ini:

`git changelog --list`

- Tampilkan daftar rentang komit yang dilakukan sejak tag komit `2.1.0` hingga komit terkini:

`git changelog --list --start-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.1.0</span>

- Tampilkan, dengan format yang mudah dibaca manusia, daftar rentang komit antara tag `0.5.0` dan `1.0.0`:

`git changelog --start-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5.0</span>` --final-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- Tampilkan, dengan format yang mudah dibaca manusia, daftar rentang komit antara komit `0b97430` dan komit yang ditandai sebagai tag `1.0.0`:

`git changelog --start-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0b97430</span>` --final-tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.0.0</span>

- Gunakan `CHANGELOG.md` untuk menyimpan informasi daftar perubahan tersebut:

`git changelog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CHANGELOG.md</span>

- Hapus dan gantikan keseluruhan isi file perubahan dengan yang baru:

`git changelog --prune-old`
