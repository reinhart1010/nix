---
layout: page
title: common/git-column (Indonesia)
description: "Tampilkan data dalam bentuk kolom."
content_hash: cbeeb9b901d33b0d484d6e5f6b56a13b2f93f715
last_modified_at: 2024-05-04
related_topics:
  - title: English version
    url: /en/common/git-column.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-column.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git column

Tampilkan data dalam bentuk kolom.
Informasi lebih lanjut: <https://git-scm.com/docs/git-column>.

- Tampilkan `stdin` dalam bentuk beberapa kolom:

`ls | git column --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">column</span>

- Tampilkan `stdin` sebagai beberapa kolom dengan lebar maksimum sebesar `100`:

`ls | git column --mode=column --width=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- Tampilkan `stdin` sebagai beberapa kolom dengan padding maksimum sebesar `30`:

`ls | git column --mode=column --padding=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
