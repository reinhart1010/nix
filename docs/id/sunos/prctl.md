---
layout: page
title: sunos/prctl (Indonesia)
description: "Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan."
content_hash: 42ac72cdc2ef0918f12e388c8fd6677ae26ba2f4
last_modified_at: 2024-04-09
related_topics:
  - title: English version
    url: /en/sunos/prctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/prctl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/prctl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/prctl.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/prctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/sunos/prctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># prctl

Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan.
Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1/prctl>.

- Periksa batas dan perizinan proses:

`prctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Periksa batas dan perizinan proses dalam format yang dapat diurai mesin:

`prctl -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Ambil batas spesifik dari sebuah proses yang berjalan:

`prctl -n process.max-file-descriptor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>
