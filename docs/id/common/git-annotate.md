---
layout: page
title: common/git-annotate (Indonesia)
description: "Tampilkan kode hash serta pelaku komit terakhir pada setiap baris suatu file teks."
content_hash: 6d5990ac6d04f8bddf785ed72f2b2e31faceed44
last_modified_at: 2024-10-13
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
  - title: українська version
    url: /uk/common/git-annotate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git annotate

Tampilkan kode hash serta pelaku komit terakhir pada setiap baris suatu file teks.
Lihat juga `git blame`, yang lebih disarankan daripada `git annotate`.
Perintah `git annotate` disediakan bagi pengguna yang telah familiar pada sistem manajemen versi lainnya.
Informasi lebih lanjut: <https://git-scm.com/docs/git-annotate>.

- Tampilkan file teks beserta informasi nama pelaku dan kode hash komit terakhir pada akhir setiap baris teks:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Tampilkan file dengan informasi komit menggunakan alamat surel/[e]mail daripada nama pelaku:

`git annotate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--show-email</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Tampilkan hanya baris-baris teks yang memenuhi kriteria ekspresi reguler:

`git annotate -L :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ekspresi_reguler</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>
