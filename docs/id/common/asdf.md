---
layout: page
title: common/asdf (Indonesia)
description: "Alat baris perintah untuk mengatur versi paket piranti lunak yang berbeda-beda."
content_hash: 6d50553559a0a71c6dbc70c53baf21b084947ee8
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/asdf.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/asdf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asdf.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asdf.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/asdf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asdf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asdf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asdf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asdf

Alat baris perintah untuk mengatur versi paket piranti lunak yang berbeda-beda.
Informasi lebih lanjut: <https://asdf-vm.com>.

- Tampilkan seluruh plugin yang tersedia untuk dipasang:

`asdf plugin list all`

- Pasang suatu plugin:

`asdf plugin add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>

- Tampilkan seluruh versi yang tersedia terhadap suatu paket:

`asdf list all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>

- Pasang suatu paket dengan versi tertentu:

`asdf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Setel versi bawaan/default paket piranti lunak yang akan digunakan secara global (seluruh pengguna):

`asdf global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>

- Setel versi bawaan/default paket piranti lunak yang akan digunakan secara lokal (pengguna saat ini):

`asdf local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi</span>
