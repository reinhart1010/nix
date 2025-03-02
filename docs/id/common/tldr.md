---
layout: page
title: common/tldr (Indonesia)
description: "Tampilkan laman bantuan sederhana untuk alat baris perintah (command-line) dari proyek dokumentasi tldr-pages."
content_hash: 549c532b1a1128045df30cb9bf7a5a0dca84093f
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/tldr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tldr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tldr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tldr.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/tldr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/tldr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tldr.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/common/tldr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/tldr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tldr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tldr.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tldr.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/tldr.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/tldr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tldr.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tldr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tldr.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/tldr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tldr

Tampilkan laman bantuan sederhana untuk alat baris perintah (command-line) dari proyek dokumentasi tldr-pages.
Catatan: opsi `--language` dan `--list` sering diimplementasikan oleh program-program klien meskipun tak diwajibkan menurut spesifikasi teknis.
Informasi lebih lanjut: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Tampilkan laman bantuan sederhana untuk suatu perintah (catatan: beginilah cara Anda sampai di sini!):

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Tampilkan laman bantuan sederhana untuk suatu subperintah:

`tldr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subperintah</span>

- Tampilkan laman bantuan untuk suatu perintah dalam suatu bahasa (jika tersedia, selainnya dalam bahasa Inggris):

`tldr --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">kode_bahasa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>

- Tampilkan laman bantuan untuk suatu perintah pada [p]latform tujuan:

`tldr --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- M[u]takhirkan data cache lokal untuk laman-laman bantuan:

`tldr --update`

- Tampilkan daftar seluruh laman bantuan untuk perintah-perintah yang tersedia pada platform saat ini dan `common` (lintas platform):

`tldr --list`

- Tampilkan daftar seluruh laman bantuan subperintah yang tersedia untuk dokumentasi suatu perintah induk:

`tldr --list | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perintah</span>` | column`

- Tampilkan suatu laman bantuan untuk perintah yang dipilih secara acak:

`tldr --list | shuf -n1 | xargs tldr`
