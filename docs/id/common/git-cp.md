---
layout: page
title: common/git-cp (Indonesia)
description: "Salin suatu berkas menuju lokasi baru dengan menyimpan riwayat perubahan atas berkas tersebut."
content_hash: cef618ccec5af9223d3a962dc26a8f9ab57af149
last_modified_at: 2024-09-10
related_topics:
  - title: English version
    url: /en/common/git-cp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-cp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git cp

Salin suatu berkas menuju lokasi baru dengan menyimpan riwayat perubahan atas berkas tersebut.
Bagian dari `git-extras`.
Informasi lebih lanjut: <https://github.com/tj/git-extras/blob/master/Commands.md#git-cp>.

- Salin suatu berkas dalam suatu repositori Git, menuju tujuan pada direktori yang sama:

`git cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_berkas_baru</span>

- Salin berkas menuju tujuan yang lain:

`git cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_baru</span>
