---
layout: page
title: common/git-bugreport (Indonesia)
description: "Tangkap dan simpan informasi sistem dan pengguna Git dalam berkas teks untuk kepentingan melaporkan dan menyelesaikan masalah/bug internal dalam Git."
content_hash: 80c28683912fd873f14b5aee57ebc74a391f104f
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/git-bugreport.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bugreport.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-bugreport.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git bugreport

Tangkap dan simpan informasi sistem dan pengguna Git dalam berkas teks untuk kepentingan melaporkan dan menyelesaikan masalah/bug internal dalam Git.
Informasi lebih lanjut: <https://git-scm.com/docs/git-bugreport>.

- Buat berkas laporan masalah/bug baru pada direktori saat ini:

`git bugreport`

- Buat berkas laporan pada direktori tertentu, dan buat direktori tersebut jika belum:

`git bugreport --output-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>

- Buat berkas laporan baru, dengan nama berkas diakhiri dengan tanggal pelaporan menurut format `strftime`:

`git bugreport --suffix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%m%d%y</span>
