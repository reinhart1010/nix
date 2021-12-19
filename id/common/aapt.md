---
layout: page
title: common/aapt (Indonesia)
description: "Alat Pemaketan Android Asset."
content_hash: 1d98db8157a36ba57c46a2804106239d1b683d65
related_topics:
  - title: Deutsch version
    url: /de/common/aapt.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aapt.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aapt.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aapt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aapt.html
    icon: bi bi-globe
---
# aapt

Alat Pemaketan Android Asset.
Menyusun dan memaketkan resource aplikasi Android.
Informasi lebih lanjut: <https://elinux.org/Android_aapt>.

- Daftar berkas-berkas yang termuat dalam arsip APK:

`aapt list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/aplikasi.apk</span>

- Menampilkan metadata aplikasi (versi, izin, dsb.):

`aapt dump badging `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/aplikasi.apk</span>

- Membuat arsip APK baru dengan berkas dari direktory yang ditentukan:

`aapt package -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/aplikasi.apk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alamat/ke/direktori</span>
