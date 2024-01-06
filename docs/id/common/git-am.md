---
layout: page
title: common/git-am (Indonesia)
description: "Gunakan perubahan dari file deskripsi perubahan (patch) untuk melakukan sebuah komit. Dapat digunakan untuk menerima komit melalui surel/email."
content_hash: ad11c2235987762af91f03488f3b4b0c848d319a
last_modified_at: 2024-01-06
related_topics:
  - title: Deutsch version
    url: /de/common/git-am.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-am.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-am.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-am.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-am.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-am.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-am.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-am.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-am.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git am

Gunakan perubahan dari file deskripsi perubahan (patch) untuk melakukan sebuah komit. Dapat digunakan untuk menerima komit melalui surel/email.
Lihat juga `git format-patch` untuk membuat file deskripsi perubahan/patch.
Informasi lebih lanjut: <https://git-scm.com/docs/git-am>.

- Gunakan dan komit perubahan dari file patch dalam direktori lokal:

`git am `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.patch</span>

- Gunakan dan komit perubahan dari file patch dari sumber dalam jaringan (online):

`curl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/file.patch</span>` | git apply`

- Batalkan proses perubahan yang dilakukan:

`git am --abort`

- Lakukan perubahan-perubahan dari file patch sebisa mungkin, dan tolak file patch jika proses tersebut gagal:

`git am --reject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file.patch</span>
