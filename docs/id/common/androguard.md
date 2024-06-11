---
layout: page
title: common/androguard (Indonesia)
description: "Lakukan rekayasa terbalik terhadap suatu aplikasi Android. Program ini ditulis dalam bahasa pemrograman Python."
content_hash: f2ec62a42cbd18ac939bb3222c95ed432e5f69e7
last_modified_at: 2024-06-11
related_topics:
  - title: English version
    url: /en/common/androguard.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/androguard.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/androguard.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/androguard.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/androguard.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/androguard.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># androguard

Lakukan rekayasa terbalik terhadap suatu aplikasi Android. Program ini ditulis dalam bahasa pemrograman Python.
Informasi lebih lanjut: <https://github.com/androguard/androguard>.

- Tampilkan manifes aplikasi Android:

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/aplikasi.apk</span>

- Tampilkan metadata aplikasi (versi dan ID aplikasi):

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/aplikasi.apk</span>

- Bongkar kode-kode program Java dari suatu aplikasi:

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/aplikasi.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori</span>
