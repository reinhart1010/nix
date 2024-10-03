---
layout: page
title: common/autojump (Indonesia)
description: "Lompat dengan cepat menuju direktori-direktori yang paling sering anda kunjungi."
content_hash: 7933c9bad5752dc8e7f559b6f36ca793ef32fc37
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/common/autojump.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autojump.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autojump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/autojump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autojump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autojump

Lompat dengan cepat menuju direktori-direktori yang paling sering anda kunjungi.
Alias seperti j atau jc sudah disediakan untuk mengurangi pengetikan.
Informasi lebih lanjut: <https://github.com/wting/autojump>.

- Lompat menuju direktori yang mengandung pola yang diberikan:

`j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola</span>

- Lompat menuju sub-direktori (anak) dari direktori saat ini yang mengandung pola yang diberikan:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola</span>

- Buka direktori yang mengandung pola yang diberikan dalam aplikasi manajemen berkas sistem operasi:

`jo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola</span>

- Buang direktori-direktori dalam pangkalan data (database) autojump yang telah sebelumnya dihapus:

`j --purge`

- Tampilkan entri yang ada dalam pangkalan data autojump:

`j -s`
