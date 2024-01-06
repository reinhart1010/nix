---
layout: page
title: common/git-checkout-index (Indonesia)
description: "Salin file dari indeks menuju direktori kerja saat ini."
content_hash: 9c1319eba68a588fefa6427de25b1befe832de72
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/git-checkout-index.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout-index.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout-index.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-checkout-index.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git checkout-index

Salin file dari indeks menuju direktori kerja saat ini.
Informasi lebih lanjut: <https://git-scm.com/docs/git-checkout-index>.

- Pulihkan berkas-berkas yang terhapus sejak komit terakhir:

`git checkout-index --all`

- Pulihkan berkas-berkas yang terhapus atau termodifikasi sejak komit terakhir:

`git checkout-index --all --force`

- Pulihkan berkas-berkas yang diubah sejak komit terakhir, mengabaikan berkas-berkas yang telah dihapus sebelumnya:

`git checkout-index --all --force --no-create`

- Ekspor sebuah salinan pohon (tree) pada komit terakhir kepada suatu direktori (nama direktori pada `--prefix` perlu diakhiri dengan garis miring):

`git checkout-index --all --force --prefix=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_ekspor/</span>
