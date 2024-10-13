---
layout: page
title: common/git-bugreport (Indonesia)
description: "Tangkap dan simpan informasi sistem dan pengguna Git dalam berkas teks untuk kepentingan melaporkan dan menyelesaikan masalah/bug internal dalam Git."
content_hash: df8c3823a4b509c7dc711d5f51711d07e589f2a2
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/git-bugreport.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-bugreport.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bugreport.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git bugreport

Tangkap dan simpan informasi sistem dan pengguna Git dalam berkas teks untuk kepentingan melaporkan dan menyelesaikan masalah/bug internal dalam Git.
Informasi lebih lanjut: <https://git-scm.com/docs/git-bugreport>.

- Buat berkas laporan masalah/bug baru pada direktori saat ini:

`git bugreport`

- Buat berkas laporan pada direktori tertentu, dan buat direktori tersebut jika belum:

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output-directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Buat berkas laporan baru, dengan nama berkas diakhiri dengan tanggal pelaporan menurut format `strftime`:

`git bugreport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--suffix</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%m%d%y</span>
