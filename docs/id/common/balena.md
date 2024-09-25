---
layout: page
title: common/balena (Indonesia)
description: "Lakukan interaksi dengan layanan balenaCloud, openBalena, dan balena API."
content_hash: 1648995e18cfc68adcf24abf2c77d54724d4c9dc
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/balena.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/balena.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/balena.html
    icon: bi bi-globe
tldri18n_status: 2
---
# balena

Lakukan interaksi dengan layanan balenaCloud, openBalena, dan balena API.
Informasi lebih lanjut: <https://www.balena.io/docs/reference/cli/>.

- Masuk dengan akun balenaCloud:

`balena login`

- Buat suatu aplikasi balenaCloud atau openBalena baru:

`balena app create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_aplikasi</span>

- Tampilkan daftar seluruh aplikasi yang diatur dalam akun balenaCloud atau openBalena:

`balena apps`

- Tampilkan daftar seluruh perangkat yang terhubung dengan akun balenaCloud atau openBalena:

`balena devices`

- Pasang citra balenaOS ke dalam suatu perangkat penyimpanan lokal:

`balena local flash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/balenaos.img</span>` --drive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lokasi_penyimpanan</span>
