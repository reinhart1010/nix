---
layout: page
title: linux/xterm (Indonesia)
description: "Emulator terminal untuk sistem window X."
content_hash: 7f4c0514cd0ac9064c4e936bc1bf16fced6c5cf3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/xterm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xterm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xterm

Emulator terminal untuk sistem window X.
Informasi lebih lanjut: <https://manned.org/xterm>.

- Membuka terminal dengan judul `Example`:

`xterm -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example</span>

- Membuka terminal dalam mode fullscreen:

`xterm -fullscreen`

- Membuka terminal dengan warna background biru tua dan warna foreground (warna font) kuning:

`xterm -bg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">darkblue</span>` -fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yellow</span>

- Membuka terminal dengan 100 karakter per baris dan 35 baris, di posisi layar x=200px, y=20px:

`xterm -geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">35</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Membuka terminal dengan font Serif dengan ukuran font sebesar 20:

`xterm -fa `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Serif'</span>` -fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>
