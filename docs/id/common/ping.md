---
layout: page
title: common/ping (Indonesia)
description: "Mengirim paket-paket ICMP ECHO_REQUEST ke host dalam jaringan."
content_hash: 80e7faf86b03402bb7e199e41193fefa46b4822c
related_topics:
  - title: Deutsch version
    url: /de/common/ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ping

Mengirim paket-paket ICMP ECHO_REQUEST ke host dalam jaringan.
Informasi lebih lanjut: <https://manned.org/ping>.

- Ping host:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host dalam jumlah kali tertentu:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jumlah</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host, dengan menentukan interval dalam sekian detik di antara request (asalnya 1 detik):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jumlah-detik</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host tanpa mencoba untuk melihat alamat dari nama-nama simbolis:

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Ping host dan membunyikan bel saat paket diterima (jika terminal anda mendukungnya):

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Menampilkan juga pesan jika tidak ada respon yang diterima:

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>
