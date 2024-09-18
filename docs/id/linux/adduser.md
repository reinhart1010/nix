---
layout: page
title: linux/adduser (Indonesia)
description: "Utilitas penambahan pengguna."
content_hash: 6c5931c8fb4442c7926c9ec33fed203133dcf2d5
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/adduser.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/adduser.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adduser

Utilitas penambahan pengguna.
Informasi lebih lanjut: <https://manned.org/adduser>.

- Buat seorang pengguna baru dengan sebuah direktori pangkal/home bawaan dan mendesak pengguna untuk mengatur sebuah kata sandi:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>

- Buat seorang pengguna baru tanpa sebuah direktori pangkal/home:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>

- Buat seorang pengguna baru dengan sebuah direktori pangkal/home di jalur yang telah dispesifikasikan:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalur/ke/home</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>

- Buat seorang pengguna baru dengan shell yang telah dispesifikasikan sebagai shell login:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalur/ke/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>

- Buat seorang pengguna baru yang masuk ke grup pengguna yang dispesifikasikan:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_pengguna</span>
