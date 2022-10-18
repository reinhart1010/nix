---
layout: page
title: common/bat (Indonesia)
description: "Mencetak dan menggabungkan berkas."
content_hash: d9a7e420fd76b28952d675a93c45842b76f7058b
related_topics:
  - title: Deutsch version
    url: /de/common/bat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bat.html
    icon: bi bi-globe
---
# bat

Mencetak dan menggabungkan berkas.
Klon dari `cat` dengan sintaks berwarna dan integrasi Git.
Informasi lebih lanjut: <https://github.com/sharkdp/bat>.

- Mencetak konten berkas ke keluaran standar:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas</span>

- Menggabungkan konten beberapa berkas ke berkas tujuan:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_tujuan</span>

- Menambahkan konten beberapa berkas ke berkas tujuan:

`bat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_tujuan</span>

- Memberi nomor pada setiap baris keluaran:

`bat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas</span>

- Mencetak konten JSON dengan sintaks berwarna:

`bat --language json berkas.json`

- Menampilkan semua bahasa yang didukung:

`bat --list-languages`
