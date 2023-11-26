---
layout: page
title: openbsd/pkg_delete (Indonesia)
description: "Hapus pemasangan paket dalam OpenBSD."
content_hash: c74af954eb27a04535a7638808760c53b49131a6
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_delete

Hapus pemasangan paket dalam OpenBSD.
Lihat juga: `pkg_add`, `pkg_info`.
Informasi lebih lanjut: <https://man.openbsd.org/pkg_delete>.

- Hapus sebuah paket yang terpasang:

`pkg_delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Hapus paket beserta penunjang (dependency) yang juga tidak lagi dipakai:

`pkg_delete -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>

- Tampilkan apa yang terjadi ketika menghapus suatu paket tanpa memprosesnya secara langsung (dry-run):

`pkg_delete -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_paket</span>
