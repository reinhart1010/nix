---
layout: page
title: common/git-count-objects (Indonesia)
description: "Hitung jumlah objek komit yang telah dibuka beserta pemakaian ruang penyimpanan dalam direktori repositori saat ini."
content_hash: bd0ecc36bd2674bff1a76d7a7739e44baa0c5223
last_modified_at: 2024-06-10
related_topics:
  - title: English version
    url: /en/common/git-count-objects.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-count-objects.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-count-objects.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git count-objects

Hitung jumlah objek komit yang telah dibuka beserta pemakaian ruang penyimpanan dalam direktori repositori saat ini.
Informasi lebih lanjut: <https://git-scm.com/docs/git-count-objects>.

- Hitung jumlah seluruh objek dan pemakaian ruang penyimpanan:

`git count-objects`

- Hitung jumlah seluruh objek dan pemakaian ruang penyimpanan, dalam format satuan yang lebih ramah dibaca manusia:

`git count-objects --human-readable`

- Tampilkan informasi perhitungan secara lebih mendalam:

`git count-objects --verbose`

- Tampilkan informasi perhitungan secara lebih mendalam, menggunakan format satuan yang lebih ramah dibaca manusia:

`git count-objects --human-readable --verbose`
