---
layout: page
title: common/ping (Indonesia)
description: "Kirim kumpulan paket ICMP ECHO_REQUEST (sebagai pesan \"ping\") ke host dalam jaringan."
content_hash: 5021d85b485b7bfcda2e280ab7215fec873f4ea9
last_modified_at: 2024-10-26
related_topics:
  - title: Deutsch version
    url: /de/common/ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ping.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ping.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ping

Kirim kumpulan paket ICMP ECHO_REQUEST (sebagai pesan "ping") ke host dalam jaringan.
Informasi lebih lanjut: <https://manned.org/ping>.

- Ping suatu host:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping suatu host dengan jumlah pengulangan yang ditetapkan:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jumlah</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping suatu host, dengan menentukan interval dalam sekian detik di antara permintaan (asalnya 1 detik):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping suatu host tanpa mencoba untuk melihat alamat dari nama-nama simbolis:

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping suatu host dan membunyikan bel saat paket diterima (jika terminal anda mendukungnya):

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Tampilkan juga pesan jika tidak ada respon yang diterima:

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping suatu host dengan jumlah pengulangan yang ditetapkan, batas timeout (`-W`) untuk setiap balasan, serta batas waktu (`-w`) eksekusi bagi keseluruhan proses ping berjalan:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jumlah</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detik</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
