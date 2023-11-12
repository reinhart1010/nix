---
layout: page
title: common/ping (Indonesia)
description: "Mengirim paket-paket ICMP ECHO_REQUEST ke host dalam jaringan."
content_hash: 80e7faf86b03402bb7e199e41193fefa46b4822c
last_modified_at: 2023-11-12
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

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
