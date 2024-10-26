---
layout: page
title: common/cowsay (Indonesia)
description: "Buat dan tampilkan seni teks ASCII (ASCII art) yang menampilkan objek (secara bawaan berupa seekor sapi) yang sedang berkata atau berpikir tentang sesuatu."
content_hash: 63c4fd71c6f7e07c9421baa97a420a6b0b910076
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/cowsay.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cowsay.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cowsay.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cowsay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cowsay

Buat dan tampilkan seni teks ASCII (ASCII art) yang menampilkan objek (secara bawaan berupa seekor sapi) yang sedang berkata atau berpikir tentang sesuatu.
Informasi lebih lanjut: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Tampilkan suatu seni ASCII yang menunjukkan seekor sapi berkata "halo, dunia":

`cowsay "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">halo, dunia</span>`"`

- Tampilkan seni ASCII sapi dengan pesan dari `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">halo, dunia</span>`" | cowsay`

- Tampilkan seluruh variasi seni ASCII yang tersedia:

`cowsay -l`

- Tampilkan pesan "halo, dunia" dengan variasi seni tertentu:

`cowsay -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variasi</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">halo, dunia</span>`"`

- Tampilkan seni ASCII seekor sapi yang tewas dan berpikir:

`cowthink -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Saya hanya seekor sapi, bukan pemikir hebat...</span>`"`

- Tampilkan pesan "halo, dunia" sebagai seni ASCII sapi dengan karakter yang ditentukan sebagai mata sang sapi:

`cowsay -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">karakter_mata</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">halo, dunia</span>`"`
