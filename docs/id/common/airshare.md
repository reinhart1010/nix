---
layout: page
title: common/airshare (Indonesia)
description: "Pindahkan data antara dua perangkat dalam jaringan lokal yang sama."
content_hash: b27de95b80877e9a4454e8af8501a2c62849e81e
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/airshare.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airshare.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airshare.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airshare.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/airshare.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># airshare

Pindahkan data antara dua perangkat dalam jaringan lokal yang sama.
Informasi lebih lanjut: <https://airshare.rtfd.io/en/latest/cli.html>.

- Kirim kumpulan file atau direktori:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_berbagi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...</span>

- Terima file:

`airshare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_berbagi</span>

- Nyalakan `airshare` sebagai server penerima (sehingga memungkingkan Anda untuk mengunggah melalui situs web internal):

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_berbagi</span>

- Unggah kumpulan file atau direktori menuju server penerima:

`airshare --upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_berbagi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...</span>

- Kirim file dengan alamat-alamat yang disalin pada papan klip (clipboard):

`airshare --file-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_berbagi</span>

- Terima dan salin file menuju papan klip:

`airshare --clip-receive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_berbagi</span>
