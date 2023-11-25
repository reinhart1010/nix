---
layout: page
title: openbsd/pkg_info (Indonesia)
description: "Lihat dokumentasi mengenai paket yang tersedia baik dalam repositori atau pemasangan OpenBSD."
content_hash: 830a8fd6eaafa9c779be6f3b4a13ee06fd0f4c2b
last_modified_at: 2023-11-25
related_topics:
  - title: English version
    url: /en/openbsd/pkg_info.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_info.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/pkg_info.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg_info

Lihat dokumentasi mengenai paket yang tersedia baik dalam repositori atau pemasangan OpenBSD.
Lihat juga: `pkg_add`, `pkg_delete`.
Informasi lebih lanjut: <https://man.openbsd.org/pkg_info>.

- Cari detail paket yang tersedia dalam repositori menurut namanya:

`pkg_info -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan dan simpan daftar paket yang telah terpasang, untuk digunakan dalam `pkg_add -l`:

`pkg_info -mz`
