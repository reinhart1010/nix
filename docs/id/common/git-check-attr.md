---
layout: page
title: common/git-check-attr (Indonesia)
description: "Tampilkan daftar jalur direktori (pathname) beserta atribut internal Git (gitattribute) yang diasosiasikan terhadap direktori tersebut."
content_hash: c0b3aa67e4661948b5ffed946bbe9b27add6fa63
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/git-check-attr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-check-attr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git check-attr

Tampilkan daftar jalur direktori (pathname) beserta atribut internal Git (gitattribute) yang diasosiasikan terhadap direktori tersebut.
Informasi lebih lanjut: <https://git-scm.com/docs/git-check-attr>.

- Tampilkan informasi seluruh atribut Git dalam suatu berkas:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Cek nilai suatu atribut Git dalam suatu berkas:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atribut</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas</span>

- Cek nilai seluruh atribut Git dalam kumpulan berkas:

`git check-attr --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>

- Cek nilai suatu atribut Git dalam kumpulan berkas:

`git check-attr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atribut</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jalan/menuju/berkas1 jalan/menuju/berkas2 ...</span>
