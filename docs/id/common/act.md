---
layout: page
title: common/act (Indonesia)
description: "Jalankan GitHub Actions secara lokal melalui Docker."
content_hash: c3669e447bf6e8112f8588d4c89f996d180c411d
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/act.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># act

Jalankan GitHub Actions secara lokal melalui Docker.
Informasi lebih lanjut: <https://github.com/nektos/act>.

- Tampilkan daftar actions (tugas dalam GitHub Actions) yang tersedia:

`act -l`

- Jalankan tugas dengan event default:

`act`

- Jalankan event pemicu tugas tertentu:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jenis_event</span>

- Jalankan tugas/[a]ction tertentu:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">action_id</span>

- Tampilkan tugas-tugas yang akan dijalankan ta[n]pa mengeksekusikannya (dry-run):

`act -n`

- Tampilkan log tingkat [v]erbose:

`act -v`

- Jalankan [W]orkflow tertentu:

`act push -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalam/menuju/workflow</span>
