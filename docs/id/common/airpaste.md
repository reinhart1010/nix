---
layout: page
title: common/airpaste (Indonesia)
description: "Bagikan pesan dan file dalam jaringan yang sama menggunakan mDNS."
content_hash: 2f5bf71dcbbeb4d6e88d7b3f37dbb033195b68f3
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/airpaste.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airpaste.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airpaste.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/airpaste.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/airpaste.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airpaste.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airpaste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airpaste.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/airpaste.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># airpaste

Bagikan pesan dan file dalam jaringan yang sama menggunakan mDNS.
Informasi lebih lanjut: <https://github.com/mafintosh/airpaste>.

- Tunggu untuk pesan baru dan tampilkan pesan jika diterimanya:

`airpaste`

- Kirim teks menuju jaringan:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">teks</span>` | airpaste`

- Kirim sebuah file:

`airpaste < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Terima pesan dalam bentuk file:

`airpaste > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/file</span>

- Buat atau masuk kepada suatu kanal penerimaan pesan:

`airpaste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nama_kanal</span>
