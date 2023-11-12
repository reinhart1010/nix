---
layout: page
title: common/cat (Indonesia)
description: "Mencetak dan menggabungkan berkas."
content_hash: 742e18794edb76ca3dce5ca407151b1de908c518
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cat.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cat.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cat.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cat

Mencetak dan menggabungkan berkas.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/cat>.

- Mencetak konten berkas ke keluaran standar:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas</span>

- Menggabungkan konten beberapa berkas ke berkas tujuan:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkasw</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_tujuan</span>

- Menambahkan konten beberapa berkas ke berkas tujuan:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas_tujuan</span>

- Memberi nomor pada semua baris keluaran:

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas</span>

- Menampilkan karakter yang tidak dapat dicetak dan spasi (dengan awalan `M-`jika non-ASCII):

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas</span>
