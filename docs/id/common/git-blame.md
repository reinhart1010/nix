---
layout: page
title: common/git-blame (Indonesia)
description: "Tampilkan informasi kode hash dan pelaku komit terakhir pada setiap baris dalam suatu berkas teks."
content_hash: 217d014015db9387693b84fa078ebc86e75abd2e
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/git-blame.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-blame.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-blame.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-blame.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-blame.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-blame.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-blame.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-blame.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-blame.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git blame

Tampilkan informasi kode hash dan pelaku komit terakhir pada setiap baris dalam suatu berkas teks.
Informasi lebih lanjut: <https://git-scm.com/docs/git-blame>.

- Tampilkan berkas teks beserta informasi nama pelaku dan kode hash komit terakhir pada akhir setiap baris teks:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan berkas dengan informasi komit menggunakan alamat surel/email daripada nama pelaku:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--show-email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada berkas yang disimpan dalam komit tertentu:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan informasi nama pelaku dan kode hash komit terakhir pada berkas yang disimpan sebelum komit tertentu:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komit</span>`~ `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>
