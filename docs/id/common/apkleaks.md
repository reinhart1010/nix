---
layout: page
title: common/apkleaks (Indonesia)
description: "Pindai berkas APK (aplikasi Android) untuk mencari URI, alur pemanggilan (endpoint), dan konfigurasi rahasia."
content_hash: bb0a63d5dc9676a1a8a918a7d7415247f7c97f86
last_modified_at: 2024-06-14
related_topics:
  - title: English version
    url: /en/common/apkleaks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/apkleaks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apkleaks

Pindai berkas APK (aplikasi Android) untuk mencari URI, alur pemanggilan (endpoint), dan konfigurasi rahasia.
Catatan: APKLeaks menggunakan `jadx` untuk membongkar kode aplikasi Android.
Informasi lebih lanjut: <https://github.com/dwisiswant0/apkleaks>.

- Pindai berkas ([f]ile) APK untuk mencari daftar endpoint dan kode konfigurasi rahasia:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>

- Pindai dan simpan luaran ([o]utput) ke dalam suatu berkas:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas_output.txt</span>

- Berikan [a]rgumen perintah tambahan untuk `jadx`:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas.apk</span>` --args "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--threads-count 5 --deobf</span>`"`
