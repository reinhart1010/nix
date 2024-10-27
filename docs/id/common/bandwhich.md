---
layout: page
title: common/bandwhich (Indonesia)
description: "Tampilkan penggunaan jaringan saat ini berdasarkan proses, koneksi, atau IP/nama host jarak jauh."
content_hash: 7739eb548549e012043c390b34c33ac997fa3e35
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/bandwhich.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bandwhich.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bandwhich

Tampilkan penggunaan jaringan saat ini berdasarkan proses, koneksi, atau IP/nama host jarak jauh.
Informasi lebih lanjut: <https://github.com/imsnif/bandwhich>.

- Tampilkan saja daftar alamat jarak jauh (remote address) yang dihubungi dalam bentuk tabel:

`bandwhich --addresses`

- Tampilkan daftar proses pencarian DNS:

`bandwhich --show-dns`

- Tampilkan informasi total penggunaan (kumulatif):

`bandwhich --total-utilization`

- Tampilkan informasi pemanfaatan jaringan untuk suatu antarmuka jaringan:

`bandwhich --interface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- Tampilkan daftar proses pencarian DNS yag dilakukan kepada server DNS tertentu:

`bandwhich --show-dns --dns-server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat_ip_peladen_dns</span>
