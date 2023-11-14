---
layout: page
title: openbsd/pkg_delete (Indonesia)
description: "Hapus pemasangan paket dalam OpenBSD."
content_hash: c74af954eb27a04535a7638808760c53b49131a6
last_modified_at: 2023-11-14
related_topics:
  - title: English version
    url: /en/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_delete.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/pkg_delete.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg_delete

Hapus pemasangan paket dalam OpenBSD.
Lihat juga: `pkg_add`, `pkg_info`.
Informasi lebih lanjut: <https://man.openbsd.org/pkg_delete>.

- Hapus sebuah paket yang terpasang:

`pkg_delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket beserta penunjang (dependency) yang juga tidak lagi dipakai:

`pkg_delete -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan apa yang terjadi ketika menghapus suatu paket tanpa memprosesnya secara langsung (dry-run):

`pkg_delete -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>
