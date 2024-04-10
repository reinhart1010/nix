---
layout: page
title: sunos/svccfg (Indonesia)
description: "Impor, ekspor, dan modifikasi konfigurasi servis."
content_hash: 95027aadd881b46cdec8ae6ccb06738550bf147b
last_modified_at: 2024-04-10
related_topics:
  - title: English version
    url: /en/sunos/svccfg.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svccfg.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svccfg.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svccfg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svccfg

Impor, ekspor, dan modifikasi konfigurasi servis.
Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validasi berkas konfigurasi:

`svccfg validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_smf.xml</span>

- Ekspor konfigurasi servis kedalam sebuah berkas:

`svccfg export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_servis</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalur/ke/berkas_smf.xml</span>

- Impor/perbarui konfigurasi servis dari berkas:

`svccfg import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_smf.xml</span>
