---
layout: page
title: common/nvim (Indonesia)
description: "Neovim, teks editor programmer berbasis Vim, menyediakan beberapa mode untuk manipulasi teks berbeda jenis."
content_hash: 63f3e57636e29d583ad7d71638990a7a5596c81b
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/nvim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nvim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nvim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nvim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvim

Neovim, teks editor programmer berbasis Vim, menyediakan beberapa mode untuk manipulasi teks berbeda jenis.
Tekan `i` masuk mode edit. `<Esc>` kembali ke mode normal, yang tidak mengizinkan penyisipan teks biasa.
Informasi lebih lanjut: <https://neovim.io>.

- Membuka berkas:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">berkas</span>

- Masuk ke mode pengeditan teks (insert mode):

`<Esc>i`

- Menyalin ("yank") atau memotong ("delete") baris saat ini (tempel itu dengan `P`):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- Batalkan operasi terakhir:

`<Esc>u`

- Mencari sebuah pattern pada berkas (tekan `n`/`N` untuk pergi ke kecocokan berikutnya/sebelumnya):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_pencarian</span>`<Enter>`

- Melakukan penggantian ekspresi reguler pada seluruh berkas:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pengganti</span>`/g<Enter>`

- Menyimpan (write) berkas, dan keluar:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter></span>

- Keluar tanpa menyimpan:

`<Esc>:q!<Enter>`
