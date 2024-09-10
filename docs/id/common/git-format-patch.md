---
layout: page
title: common/git-format-patch (Indonesia)
description: "Buat berkas-berkas .patch dari kumpulan komit Git. Dapat dipakai untuk mengirimkan perubahan/komit melalui surel/email."
content_hash: 11252d1a50a45735001e9be7741d698a49122af0
last_modified_at: 2024-09-10
related_topics:
  - title: Deutsch version
    url: /de/common/git-format-patch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-format-patch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-format-patch.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-format-patch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-format-patch.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-format-patch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-format-patch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git format-patch

Buat berkas-berkas .patch dari kumpulan komit Git. Dapat dipakai untuk mengirimkan perubahan/komit melalui surel/email.
Lihat juga `git am`, yang memungkinkan pengguna untuk melakukan perubahan melalui berkas komit .patch yang dibuat.
Informasi lebih lanjut: <https://git-scm.com/docs/git-format-patch>.

- Buat suatu berkas `.patch` untuk mencatat seluruh komit yang belum dikirimkan (push) ke remote, menggunakan nama berkas otomatis:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">origin</span>

- Tampilkan isi berkas `.patch` menuju `stdout` yang mengandung perubahan antara dua revisi/komit:

`git format-patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisi_1</span>`..`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisi_2</span>

- Tulis suatu berkas `.patch` yang mengandung segala perubahan dalam 3 komit terakhir:

`git format-patch -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>
