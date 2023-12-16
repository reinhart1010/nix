---
layout: page
title: common/ag (Indonesia)
description: "The Silver Searcher. Seperti `ack`, namun bertujuan untuk lebih cepat daripadanya."
content_hash: 582b9ddd66755aab00f0ff4048cff5396a6c0483
last_modified_at: 2023-12-16
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ag.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ag.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ag.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ag.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ag

The Silver Searcher. Seperti `ack`, namun bertujuan untuk lebih cepat daripadanya.
Informasi lebih lanjut: <https://github.com/ggreer/the_silver_searcher>.

- Cari file yang mengandung teks "foo", dan cetak baris teks yang cocok:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Cari file yang mengandung teks "foo" dalam direktori tertentu:

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Cari file yang mengandung teks "foo", namun hanya tampilkan daftar nama file saja:

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Cari file yang mengandung teks "FOO" tanpa memerhatikan perbedaan huruf besar-kecil (case-[i]nsensitive), dan hanya cetak teks yang cocok (jangan cetak kata-kata lainnya meskipun dalam baris yang sama):

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- Cari file yang memiliki nama "bar" dan mengandung teks "foo":

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Cari file yang memiliki teks yang memenuhi kriteria ekspresi reguler:

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- Cari file dengan nama yang memiliki teks "foo":

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
