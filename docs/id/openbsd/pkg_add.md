---
layout: page
title: openbsd/pkg_add (Indonesia)
description: "Pasang/perbarui paket dalam OpenBSD."
content_hash: 5c40cd81e163d4e55c1e8ce7187f85c1f69231ad
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/openbsd/pkg_add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/pkg_add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkg_add

Pasang/perbarui paket dalam OpenBSD.
Lihat juga: `pkg_info`, `pkg_delete`.
Informasi lebih lanjut: <https://man.openbsd.org/pkg_add>.

- Perbarui seluruh paket yang terpasang, termasuk penunjangnya (dependencies):

`pkg_add -u`

- Pasang paket baru:

`pkg_add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Pasang paket menurut informasi paket yang dikeluarkan dari `pkg_info`:

`pkg_add -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_hasil_pkg_info</span>
