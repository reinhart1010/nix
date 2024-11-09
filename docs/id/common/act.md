---
layout: page
title: common/act (Indonesia)
description: "Jalankan GitHub Actions secara lokal melalui Docker."
content_hash: 113a7a026fc8dd26742954d5490c6621dedf328e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
tldri18n_status: 2
---
# act

Jalankan GitHub Actions secara lokal melalui Docker.
Informasi lebih lanjut: <https://github.com/nektos/act>.

- Tampilkan daftar actions (tugas dalam GitHub Actions) yang tersedia:

`act -l`

- Jalankan tugas dengan event default:

`act`

- Jalankan event pemicu tugas tertentu:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jenis_event</span>

- Jalankan tugas/[j]ob tertentu:

`act -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">job_id</span>

- Tampilkan tugas-tugas yang akan dijalankan ta[n]pa mengeksekusikannya (dry-run):

`act -n`

- Tampilkan log tingkat [v]erbose:

`act -v`

- Jalankan [W]orkflow tertentu:

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/workflow</span>
