---
layout: page
title: common/warp-diag (Indonesia)
description: "Alat diagnostik dan umpan balik bagi layanan Cloudflare WARP."
content_hash: 33b705efc49da30527558d90552309b89ec46b9a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/warp-diag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# warp-diag

Alat diagnostik dan umpan balik bagi layanan Cloudflare WARP.
Lihat juga: `warp-cli`.
Informasi lebih lanjut: <https://developers.cloudflare.com/warp-client/>.

- Membuat sebuah file arsip (zip) berisi informasi konfigurasi sistem dan log debug terhadap koneksi WARP:

`warp-diag`

- Membuat sebuah file arsip diagnostik dengan membubuhkan stempel waktu ke dalam nama file:

`warp-diag --add-ts`

- Menyimpan file arsip diagnostik ke dalam direktori tertentu:

`warp-diag --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Memberikan saran kepada Cloudflare WARP secara interaktif:

`warp-diag feedback`
