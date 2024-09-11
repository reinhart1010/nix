---
layout: page
title: common/git-rm (Indonesia)
description: "Hapus berkas-berkas dari indeks repositori dan sistem manajemen berkas (filesystem) lokal."
content_hash: 3d6a51316853f7a8313693ca6d12fc9b72085331
last_modified_at: 2024-09-11
related_topics:
  - title: Deutsch version
    url: /de/common/git-rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-rm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rm

Hapus berkas-berkas dari indeks repositori dan sistem manajemen berkas (filesystem) lokal.
Informasi lebih lanjut: <https://git-scm.com/docs/git-rm>.

- Hapus berkas dari indeks repositori dan filesystem lokal:

`git rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Hapus suatu direktori:

`git rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Hapus suatu berkas dari indeks repositori tanpa menghapusnya pada filesystem lokal:

`git rm --cached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
