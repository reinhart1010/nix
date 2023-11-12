---
layout: page
title: common/pip3 (Indonesia)
description: "Pengelola paket Python."
content_hash: 1dcc3dd2dc2c5cc636c1836bc28ef34a2b27bff9
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pip3.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip3.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip3.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pip3

Pengelola paket Python.
Informasi lebih lanjut: <https://pip.pypa.io>.

- Menemukan paket tersedia:

`pip3 search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Memasang paket:

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Memasang versi paket tertentu:

`pip3 install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versi_paket</span>

- Meningkatkan paket ke versi terbaru:

`pip3 install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Mencopot pemasangan paket:

`pip3 uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Menyimpan daftar paket terpasang ke berkas:

`pip3 freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Memasang paket dari berkas:

`pip3 install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Menampilkan informasi paket terinstal:

`pip3 show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>
