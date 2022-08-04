---
layout: page
title: common/nvim (Indonesia)
description: "Neovim, teks editor programmer berbasis Vim, menyediakan beberapa mode untuk manipulasi teks berbeda jenis."
content_hash: 0579d8e3a0aa2595c5dfec676b8ec2927913bbaf
related_topics:
  - title: English version
    url: /en/common/nvim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nvim.html
    icon: bi bi-globe
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

`<Esc>:wq<Enter>`

- Keluar tanpa menyimpan:

`<Esc>:q!<Enter>`
