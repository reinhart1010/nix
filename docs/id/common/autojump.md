---
layout: page
title: common/autojump (Indonesia)
description: "Melompat secara cepat ke direktori-direktori yang paling sering anda kunjungi."
content_hash: 41c42b45c723f5f6767f8f35ef148b35145b1c35
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
  - title: 中文 version
    url: /zh/common/autojump.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># autojump

Melompat secara cepat ke direktori-direktori yang paling sering anda kunjungi.
Alias seperti j atau jc sudah disediakan untuk mengurangi pengetikan.
Informasi lebih lanjut: <https://github.com/wting/autojump>.

- Melompat ke direktori yang mengandung pola yang diberikan:

`j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola</span>

- Melompat ke sub-direktori (anak) dari direktori saat ini yang mengandung pola yang diberikan:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola</span>

- Membuka direktori yang mengandung pola yang diberikan dalam file manager dari sistem operasi:

`jo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola</span>

- Membuang direktori-direktori yang tidak lagi ada dari database autojump:

`j --purge`

- Menampilkan entri yang ada di database autojump:

`j -s`
