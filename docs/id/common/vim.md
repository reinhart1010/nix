---
layout: page
title: common/vim (Indonesia)
description: "Vim (Vi IMproved), suatu aplikasi pengolah teks berbasis baris perintah, yang menyediakan beberapa mode untuk berbagai jenis proses manipulasi teks."
content_hash: 7e923f3a0ac8f1973f6c85ac03436398f46bc7e4
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/vim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vim

Vim (Vi IMproved), suatu aplikasi pengolah teks berbasis baris perintah, yang menyediakan beberapa mode untuk berbagai jenis proses manipulasi teks.
Menekan `i` dalam mode normal akan memasuki mode penyisipan (insert). Menekan `<Esc>` akan kembali ke mode normal, yang memungkinkan penggunaan perintah Vim.
Lihat juga: `vimdiff`, `vimtutor`, `nvim`.
Informasi lebih lanjut: <https://www.vim.org>.

- Buka suatu berkas:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Buka suatu berkas pada nomor baris teks tertentu:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomor_baris</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Lihat manual bantuan untuk Vim:

`:help<Enter>`

- Simpan dan keluar dari sesi pengolahan teks saat ini:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter></span>

- Masuk ke mode normal dan batalkan operasi terakhir:

`<Esc>u`

- Cari pola dalam berkas (tekan `n`/`N` untuk menuju ke kecocokan berikutnya/sebelumnya):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pola_pencarian</span>`<Enter>`

- Lakukan substitusi ekspresi reguler di seluruh berkas:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks_pengganti</span>`/g<Enter>`

- Tampilkan nomor baris:

`:set nu<Enter>`
