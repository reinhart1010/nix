---
layout: page
title: common/mongod (Indonesia)
description: "Server database MongoDB."
content_hash: 3e2d0b8ff899dbf8176bf0fd6411a5ae2b671404
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mongod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mongod.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mongod

Server database MongoDB.
Informasi lebih lanjut: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Menentukan berkas konfigurasi:

`mongod --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas</span>

- Menentukan port yang digunakan:

`mongod --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Menentukan tingkat pencatatan perilaku (*profiling*) database. 0 mati, 1 hanya operasi lambat, 2 semuanya:

`mongod --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2</span>
