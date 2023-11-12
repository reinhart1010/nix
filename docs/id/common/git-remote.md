---
layout: page
title: common/git-remote (Indonesia)
description: "Mengelola kumpulan repositori yang dilacak/diikuti (\"remotes\")."
content_hash: c81b2208d191b47624e52e61949b62a8de993cc8
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-remote.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-remote.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-remote.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-remote.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-remote.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-remote.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-remote.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git remote

Mengelola kumpulan repositori yang dilacak/diikuti ("remotes").
Informasi lebih lanjut: <https://git-scm.com/docs/git-remote>.

- Menampilkan daftar remote, namanya dan URL:

`git remote -v`

- Menampilkan informasi tentang remote:

`git remote show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>

- Menambahkan remote:

`git remote add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_remote</span>

- Mengubah URL dari remote (gunakan `--add` untuk tetap menyimpan URL lama):

`git remote set-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_baru</span>

- Menghapus remote:

`git remote remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>

- Mengubah nama remote:

`git remote rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_lama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_baru</span>
