---
layout: page
title: common/git-clean (Indonesia)
description: "Hapus berkas-berkas yang tak dilacak oleh Git pada pohon direktori kerja saat ini."
content_hash: 4b282b41897705392b252d5a958c20b190e21f93
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/git-clean.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-clean.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-clean.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-clean.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-clean.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-clean.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git clean

Hapus berkas-berkas yang tak dilacak oleh Git pada pohon direktori kerja saat ini.
Informasi lebih lanjut: <https://git-scm.com/docs/git-clean>.

- Hapus seluruh berkas yang tak dilacak:

`git clean`

- Hapus menggunakan mode interaktif:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>

- Tampilkan kumpulan berkas yang akan dihapus tanpa menghapusnya:

`git clean --dry-run`

- Hapus berkas-berkas secara paksa:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>

- Hapus kumpulan [d]irektori secara paksa:

`git clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--force</span>` -d`

- Hapus berkas-berkas yang tak dilacak, termasuk berkas yang dikecualikan (menurut daftar `.gitignore` dan `.git/info/exclude`):

`git clean -x`
