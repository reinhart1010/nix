---
layout: page
title: common/mongod (Indonesia)
description: "Peladen basis data MongoDB."
content_hash: 3d263e1752d5de1e22af83e1c5ea56843b4abcf4
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/common/mongod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mongod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mongod

Peladen basis data MongoDB.
Informasi lebih lanjut: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Tentukan direktori penyimpanan basis data (default: `/data/db` dalam Linux dan macOS, `C:\data\db` dalam Windows):

`mongod --dbpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Tentukan berkas konfigurasi basis data:

`mongod --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tentukan port yang akan digunakan (default: 27017):

`mongod --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Tentukan tingkat pencatatan perilaku (profiling) peladen basis data. 0 mati, 1 hanya operasi lambat, 2 semuanya (default: 0):

`mongod --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2</span>
