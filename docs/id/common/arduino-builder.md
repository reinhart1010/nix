---
layout: page
title: common/arduino-builder (Indonesia)
description: "Bangun program dari kode sumber piranti lunak (sketsa) Arduino."
content_hash: a1236192dec9c893d0a26d50f2c2006706e23c32
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/arduino-builder.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/arduino-builder.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/arduino-builder.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/arduino-builder.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># arduino-builder

Bangun program dari kode sumber piranti lunak (sketsa) Arduino.
PERINGATAN DEPREKASI: Alat ini sedang dihapus demi penggunaan perintah `arduino` yang baru.
Informasi lebih lanjut: <https://github.com/arduino/arduino-builder>.

- Bangun program dari suatu berkas (sketsa) kode sumber piranti lunak:

`arduino-builder -compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/sketsa.ino</span>

- Tentukan tingkat penampilan informasi awakutu (nilai bawaan: 5):

`arduino-builder -debug-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..10</span>

- Tentukan direktori untuk menampung hasil pembangunan:

`arduino-builder -build-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/direktori_hasil_pembangunan</span>

- Gunakan konfigurasi yang didefinisikan di dalam suatu berkas, daripada mendefinisikan parameter perintah seperti `-hardware` dan `-tools` berulang kali:

`arduino-builder -build-options-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/build.options.json</span>

- Gunakan mode verbose, tampilkan proses pembangunan secara rinci:

`arduino-builder -verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
