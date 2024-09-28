---
layout: page
title: common/mozillavpn (Indonesia)
description: "Layanan jaringan privat virtual (VPN) dari pembuat Firefox."
content_hash: a1c59991165a5c586b5816528c4aa47f10534df3
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/mozillavpn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mozillavpn

Layanan jaringan privat virtual (VPN) dari pembuat Firefox.
Lihat juga: `fastd`, `ivpn`, `mullvad`, `warp-cli`.
Informasi lebih lanjut: <https://github.com/mozilla-mobile/mozilla-vpn-client/wiki/Command-line-interface>.

- Masuk ke dalam akun melalui mode input interaktif:

`mozillavpn login`

- Hubungkan ke dalam jaringan Mozilla VPN:

`mozillavpn activate`

- Tampilkan status hubungan:

`mozillavpn status`

- Tampilkan daftar peladen (server) VPN yang tersedia:

`mozillavpn servers`

- Pilih peladen jaringan untuk dihubungkan:

`mozillavpn select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_peladen</span>

- Putuskan hubungan dengan layanan VPN:

`mozillavpn deactivate`

- Keluar dari akun:

`mozillavpn logout`

- Tampilkan bantuan untuk suatu subperintah:

`mozillavpn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subperintah</span>` --help`
