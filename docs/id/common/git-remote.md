---
layout: page
title: common/git-remote (Indonesia)
description: "Kelola kumpulan repositori yang dilacak/diikuti dari sumber jarak jauh (\"remotes\")."
content_hash: b24b8ceff7eb61ebd265236e2341a3f33c906301
last_modified_at: 2024-09-11
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
  - title: 한국어 version
    url: /ko/common/git-remote.html
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
tldri18n_status: 2
---
# git remote

Kelola kumpulan repositori yang dilacak/diikuti dari sumber jarak jauh ("remotes").
Informasi lebih lanjut: <https://git-scm.com/docs/git-remote>.

- Tampilkan daftar remote, namanya dan URL:

`git remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>

- Tampilkan informasi tentang suatu remote:

`git remote show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>

- Tambahkan suatu remote untuk diikuti pada repositori saat ini:

`git remote add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_remote</span>

- Ubah alamat URL dari remote (gunakan `--add` untuk tetap menyimpan URL lama):

`git remote set-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_baru</span>

- Tampilkan alamat URL dari suatu remote:

`git remote get-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>

- Hapus remote dari daftar remote yang dilacak pada repositori saat ini:

`git remote remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>

- Ubah nama remote untuk dikelola dalam repositori saat ini:

`git remote rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_lama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_baru</span>
