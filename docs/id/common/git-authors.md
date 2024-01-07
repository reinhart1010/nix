---
layout: page
title: common/git-authors (Indonesia)
description: "Buat daftar pelaku komit pada suatu repositori Git."
content_hash: ad6816b76682af409a48b484ef4bc49097cbf847
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-authors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git authors

Buat daftar pelaku komit pada suatu repositori Git.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- Tampilkan daftar pelaku komit menuju `stdout` daripada menuju ke file `AUTHORS`:

`git authors --list`

- Masukkan daftar pelaku komit menuju file `AUTHORS`, kemudian buka file tersebut pada aplikasi penyunting file teks default:

`git authors`

- Masukkan daftar pelaku komit tanpa informasi alamat surel/email menuju file `AUTHORS`, kemudian buka file tersebut pada aplikasi penyunting file teks default:

`git authors --no-email`
