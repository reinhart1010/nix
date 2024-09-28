---
layout: page
title: common/fastd (Indonesia)
description: "Program layanan daemon untuk jaringan priat virtual (VPN)."
content_hash: b411b42751c03a5a864716f3669a8d2678582b81
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/fastd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fastd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fastd

Program layanan daemon untuk jaringan priat virtual (VPN).
Bekerja baik dalam lapisan jaringan Layer 2 atau Layer 3, mendukung berbagai metode enkripsi, dan dipakai oleh Freifunk.
Lihat juga: `ivpn`, `mozillavpn`, `mullvad`, `warp-cli`.
Informasi lebih lanjut: <https://fastd.readthedocs.io/en/stable/>.

- Jalankan `fastd` dengan konfigurasi yang diatur dalam suatu berkas:

`fastd --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/fastd.conf</span>

- Jalankan suatu layanan VPN Layer 3 dengan MTU sebesar 1400, dengan konfigurasi lainnya yang diatur dalam suatu berkas:

`fastd --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tap</span>` --mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1400</span>` --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/fastd.conf</span>

- Lakukan validasi terhadap suatu berkas konfigurasi:

`fastd --verify-config --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/fastd.conf</span>

- Buat sebuah pasangan kunci untuk mengakses layanan VPN:

`fastd --generate-key`

- Tampilkan kunci publik terhadap kunci privat yang diatur dalam berkas konfigurasi:

`fastd --show-key --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/fastd.conf</span>

- Tampilkan versi program:

`fastd -v`
