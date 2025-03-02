---
layout: page
title: common/pip (Indonesia)
description: "Pengelola paket Python."
content_hash: 619aac3d87a5f30c988d82ea0b6fb030dedaadcc
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/pip.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pip

Pengelola paket Python.
Beberapa subperintah seperti `install` mempunyai dokumentasi terpisah.
Informasi lebih lanjut: <https://pip.pypa.io>.

- Pasang suatu paket (lihat dokumentasi `pip install` untuk melihat contoh pemasangan tambahan):

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Pasang suatu paket untuk hanya digunakan oleh pengguna saat ini:

`pip install --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tingkatkan suatu paket ke versi terbaru:

`pip install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Copot pemasangan suatu paket:

`pip uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Simpan daftar paket-paket terpasang ke dalam suatu berkas:

`pip freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Tampilkan informasi suatu paket yang terpasang:

`pip show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Pasang kumpulan paket dari suatu berkas:

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>
