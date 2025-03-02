---
layout: page
title: common/warp-cli (Indonesia)
description: "Program command-line resmi untuk layanan Cloudflare WARP."
content_hash: 64874f1e9832e9c6b92aa0eaf6ce5621f7ce34b3
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/warp-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# warp-cli

Program command-line resmi untuk layanan Cloudflare WARP.
WARP adalah sebuah layanan jaringan privat virtual (VPN) yang mengenkripsi lalu lintas jaringan demi meningkatkan privasi, keamanan, dan kecepatan.
Lihat juga: `fastd`, `ivpn`, `mozillavpn`, `mullvad`.
Informasi lebih lanjut: <https://developers.cloudflare.com/warp-client/>.

- Daftarkan perangkat ini ke dalam jaringan WARP (harus dijalankan pada pertama kali):

`warp-cli registration new`

- Hubungkan perangkat ini ke dalam jaringan WARP:

`warp-cli connect`

- Putuskan perangkat ini dari jaringan WARP:

`warp-cli disconnect`

- Tampilkan status koneksi WARP saat ini:

`warp-cli status`

- Pindah mode operasi koneksi layanan WARP:

`warp-cli set-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mode_operasi</span>

- Tampilkan bantuan umum:

`warp-cli help`

- Tampilkan bantuan untuk suatu subperintah:

`warp-cli help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subperintah</span>
