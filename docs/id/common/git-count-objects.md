---
layout: page
title: common/git-count-objects (Indonesia)
description: "Hitung jumlah objek komit yang telah dibuka beserta pemakaian ruang penyimpanan dalam direktori repositori saat ini."
content_hash: bd0ecc36bd2674bff1a76d7a7739e44baa0c5223
last_modified_at: 2024-06-11
related_topics:
  - title: English version
    url: /en/common/git-count-objects.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-count-objects.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git count-objects

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
