---
layout: page
title: common/mv (Indonesia)
description: "Pindahkan atau namai-ulang berkas dan direktori."
content_hash: d98fed3c51bb2d4aad612ce3ee43102b6fbaef81
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/mv.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mv.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mv.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mv.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/mv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mv.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/mv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mv

Pindahkan atau namai-ulang berkas dan direktori.
Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Pindahkan berkas ke lokasi yang baru:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tujuan</span>

- Pindahkan berkas atau direktori ke dalam direktori lain yang telah ada:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Pindahkan berkas majemuk ke dalam direktori lain yang telah ada, dengan menyimpan nama masing-masing file secara utuh:

`mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber1 jalan/menuju/sumber2 ...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Pindahkan tanpa meminta konfirmasi sebelum menimpa file yang sudah ada:

`mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tujuan</span>

- Minta konfirmasi sebelum menimpa berkas yang sudah ada, tanpa memerhatikan hak akses hedua file tersebut:

`mv --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tujuan</span>

- Jangan menimpa file yang sudah ada di direktori tujuan:

`mv --no-clobber `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tujuan</span>

- Pindahkan berkas dalam mode [v]erbose, tampilkan berkas-berkas yang dipindahkan:

`mv --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sumber</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/tujuan</span>

- Tetapkan direktori tujuan ([t]arget) agar Anda dapat menggunakan alat atau perintah eksternal untuk mengelola kumpulan berkas yang dapat dipindahkan:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find /var/log -type f -name '*.log' -print0</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs -0</span>` mv --target-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_tujuan</span>
