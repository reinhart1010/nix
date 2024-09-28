---
layout: page
title: common/ffsend (Indonesia)
description: "Bagikan berkas-berkas secara mudah dan aman."
content_hash: a9e224a9883734e1662e82aef25f807bcf4128a2
last_modified_at: 2024-09-28
related_topics:
  - title: Deutsch version
    url: /de/common/ffsend.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ffsend.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ffsend.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffsend

Bagikan berkas-berkas secara mudah dan aman.
Informasi lebih lanjut: <https://gitlab.com/timvisee/ffsend>.

- Unggah suatu berkas:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Unduh suatu berkas:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Unggah berkas dengan suatu kata sandi:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>

- Unduh berkas yang terlindungi dengan suatu kata sandi:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_sandi</span>

- Unggah dan atur unggahan supaya hanya dapat diunduh sebanyak 4 kali:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--downloads</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
