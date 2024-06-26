---
layout: page
title: common/git-commit-tree (Indonesia)
description: "Alat untuk membuat objek komit secara tingkat rendah (low-level)."
content_hash: 05bd2ed98133fece618e27afdabafb7829ecebe7
last_modified_at: 2024-06-11
related_topics:
  - title: English version
    url: /en/common/git-commit-tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-commit-tree.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit-tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git commit-tree

Alat untuk membuat objek komit secara tingkat rendah (low-level).
Lihat juga: `git commit`.
Informasi lebih lanjut: <https://git-scm.com/docs/git-commit-tree>.

- Buat objek komit baru dengan pesan tertentu:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`"`

- Buat objek komit dengan pesan yang disimpan dalam suatu berkas (gunakan `-` untuk membaca dari `stdin`):

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Buat sebuah objek komit yang ditandatangani oleh kunci enkripsi GPG:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pesan</span>`" --gpg-sign`

- Buat sebuah objek komit dengan komit induk tertentu:

`git commit-tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tree</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>`" -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_hash_sha_atas_komit_induk</span>
