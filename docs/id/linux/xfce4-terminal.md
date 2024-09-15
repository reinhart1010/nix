---
layout: page
title: linux/xfce4-terminal (Indonesia)
description: "Emulator terminal XFCE4."
content_hash: b9073a77d560dd7933ce6a90370756f0ae488050
last_modified_at: 2024-09-15
related_topics:
  - title: English version
    url: /en/linux/xfce4-terminal.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xfce4-terminal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xfce4-terminal

Emulator terminal XFCE4.
Informasi lebih lanjut: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- Membuka jendela terminal baru:

`xfce4-terminal`

- Mengatur judul awal:

`xfce4-terminal --initial-title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">judul_awal</span>`"`

- Membuka tab baru di jendela terminal saat ini:

`xfce4-terminal --tab`

- Jalankan sebuah perintah di jendela terminal baru:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah_dengan_argumen</span>`"`

- Tetap buka terminal setelah perintah yang dijalankan selesai:

`xfce4-terminal --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah_dengan_argumen</span>`" --hold`

- Membuka beberapa tab baru dan menjalankan perintah di masing-masing tab:

`xfce4-terminal --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah_a</span>`" --tab --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah_b</span>`"`
