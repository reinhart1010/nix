---
layout: page
title: common/base32 (Türkçe)
description: "Bir dosya veya standart veriyi Base32 formatında şifrele veya yalın veri çıktısı olarak deşifre et."
content_hash: 1f1391ad8937dfaa75f973853aef13725ac7df1e
last_modified_at: 2024-03-17
related_topics:
  - title: English version
    url: /en/common/base32.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base32.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base32.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/base32.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/base32.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base32.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/base32.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base32.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base32

Bir dosya veya standart veriyi Base32 formatında şifrele veya yalın veri çıktısı olarak deşifre et.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/base32>.

- Bir dosyayı şifrele:

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosyaismi</span>

- Bir dosyayı deşifre et:

`base32 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosyaismi</span>

- `stdin`'den şifrele:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">herhangibirkomut</span>` | base32`

- `stdin`'den deşifre et:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">herhangibirkomut</span>` | base32 --decode`
