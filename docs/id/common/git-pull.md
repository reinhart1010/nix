---
layout: page
title: common/git-pull (Indonesia)
description: "Tarik cabang dari repositori remote and menggabungkan ke repositori lokal"
content_hash: 50569e71f180cf18814c7801c7c4fa3773f8e928
related_topics:
  - title: Deutsch version
    url: /de/common/git-pull.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-pull.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-pull.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-pull.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-pull.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-pull.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-pull.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git pull

Tarik cabang dari repositori remote and menggabungkan ke repositori lokal
Informasi lebih lanjut: <https://git-scm.com/docs/git-pull>.

- Unduh perubahan dari bawaan repositori remote dan menggabungkannya:

`git pull`

- Unduh perubahan dari bawaan repositori remote dan menggunakan maju cepat:

`git pull --rebase`

- Unduh perubahan dari repositori remote dan cabang yang diberikan, kemudian menggabungkannya ke HEAD:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_remote</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cabang</span>
