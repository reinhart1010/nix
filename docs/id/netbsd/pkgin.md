---
layout: page
title: netbsd/pkgin (Indonesia)
description: "Atur pemasangan paket `pkgsrc` dalam NetBSD."
content_hash: 97f239681bc8cab8e2ab3909fa73fe27d275e16c
last_modified_at: 2023-11-14
related_topics:
  - title: English version
    url: /en/netbsd/pkgin.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/netbsd/pkgin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/netbsd/pkgin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkgin

Atur pemasangan paket `pkgsrc` dalam NetBSD.
Informasi lebih lanjut: <https://pkgin.net/#usage>.

- Pasang sebuah paket:

`pkgin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket yang dipasang beserta penunjangnya (dependencies):

`pkgin remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Perbarui seluruh paket yang terpasang:

`pkgin full-upgrade`

- Cari paket yang tersedia dalam repositori:

`pkgin search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kata_kunci</span>

- Tampilkan daftar paket yang terpasang:

`pkgin list`

- Hapus paket-paket penunjang (dependencies) yang sudah tidak terpakai:

`pkgin autoremove`
