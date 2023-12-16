---
layout: page
title: common/ack (Indonesia)
description: "Sebuah alat pencari teks seperti `grep` yang dikhususkan bagi para pengembang perangkat lunak."
content_hash: c379b588f9c582164507c75c3a8b82e0f4815a30
last_modified_at: 2023-12-16
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ack

Sebuah alat pencari teks seperti `grep` yang dikhususkan bagi para pengembang perangkat lunak.
Lihat juga: `rg`, yang dapat mencari dengan lebih cepat.
Informasi lebih lanjut: <https://beyondgrep.com/documentation>.

- Cari file dalam direktori saat ini yang mengandung string atau kriteria dalam ekspresi reguler:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Cari tanpa mementingkan perbedaan huruf besar-kecil dalam kriteria (case-insensitive):

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Cari untuk baris-baris dalam file yang memenuhi kriteria, namun hanya cetak teks yang memenuhinya saja (jangan cetak kata-kata lainnya meskipun dalam baris yang sama):

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Hanya cari file dengan tipe tertentu (seperti `ruby` untuk mencari file `.rb`,`.erb`, `.rake`, `Rakefile` dan sebagainya):

`ack --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Jangan cari file dengan tipe tertentu:

`ack --type=no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Hitung total teks/string yang ditemukan:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Hanya cetak nama file dan total penemuan dalam file tersebut saja:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`"`

- Tampilkan daftar kombinasi nilai yang dapat dipakai dalam atribut `--type`:

`ack --help-types`
