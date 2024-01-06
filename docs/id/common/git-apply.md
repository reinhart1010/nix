---
layout: page
title: common/git-apply (Indonesia)
description: "Gunakan perubahan dari file deskripsi perubahan (patch) kepada indeks perubahan tanpa mencatat sebuah komit."
content_hash: ed3c7f0ec97dbacbacdbb6539095c36fd3c0dc72
last_modified_at: 2024-01-06
related_topics:
  - title: Deutsch version
    url: /de/common/git-apply.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-apply.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-apply.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-apply.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-apply.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-apply.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git apply

Gunakan perubahan dari file deskripsi perubahan (patch) kepada indeks perubahan tanpa mencatat sebuah komit.
Lihat juga `git am`, yang sama-sama menggunakan perubahan dari file patch namun juga mencatatnya ke dalam sebuah komit baru.
Informasi lebih lanjut: <https://git-scm.com/docs/git-apply>.

- Tampilkan informasi lengkap (mode verbose) atas proses perubahan yang sedang dilakukan:

`git apply --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Gunakan patch dan tambahkan file yang diubah ke dalam indeks perubahan:

`git apply --index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Gunakan perubahan dari file patch dari sumber dalam jaringan (online):

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- Tampilkan informasi statistik perbedaan (diffstat) setelah melakukan perubahan menurut file patch:

`git apply --stat --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Batalkan perubahan yang dilakukan melalui file patch:

`git apply --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Simpan hasil perubahan ke dalam indeks perubahan tanpa merubah susunan file/direktori dalam direktori kerja saat ini:

`git apply --cache `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>
