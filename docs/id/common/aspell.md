---
layout: page
title: common/aspell (Indonesia)
description: "Mesin pengecek ejaan secara interaktif."
content_hash: cae34962b69ace15345031486c3c4ac969e632f2
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/aspell.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aspell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aspell.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aspell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aspell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aspell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aspell

Mesin pengecek ejaan secara interaktif.
Informasi lebih lanjut: <http://aspell.net/>.

- Lakukan pengecekan ejaan terhadap suatu berkas:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Tampilkan daftar kata dalam `stdin` yang dicurigai memiliki kesalahan ejaan:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` | aspell list`

- Tampilkan daftar kamus dan bahasa yang didukung:

`aspell dicts`

- Jalankan `aspell` dengan bahasa teks yang berbeda (menggunakan format kode bahasa ISO 639):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- Tampilkan daftar kata dalam `stdin` yang dicurigai memiliki kesalahan ejaan dan abaikan kata yang berasal dari daftar kata pribadi (personal word list):

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">daftar-kata-pribadi.pws</span>` list`
