---
layout: page
title: common/git-annotate (Indonesia)
description: "Tampilkan kode hash serta pelaku komit terakhir pada setiap baris suatu file teks."
content_hash: 5552139a36efe3f41ae21845d78c26ae58a537b8
last_modified_at: 2024-01-06
related_topics:
  - title: English version
    url: /en/common/git-annotate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-annotate.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-annotate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-annotate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git annotate

Tampilkan kode hash serta pelaku komit terakhir pada setiap baris suatu file teks.
Lihat juga `git blame`, yang lebih disarankan daripada `git annotate`.
Perintah `git annotate` disediakan bagi pengguna yang telah familiar pada sistem manajemen versi lainnya.
Informasi lebih lanjut: <https://git-scm.com/docs/git-annotate>.

- Tampilkan file teks beserta informasi nama pelaku dan kode hash komit terakhir pada akhir setiap baris teks:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Tampilkan file dengan informasi komit menggunakan alamat surel/[e]mail daripada nama pelaku:

`git annotate -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Tampilkan hanya baris-baris teks yang memenuhi kriteria ekspresi reguler:

`git annotate -L :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>
