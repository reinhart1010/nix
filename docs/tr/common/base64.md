---
layout: page
title: common/base64 (Türkçe)
description: "Bir dosya veya standart veriyi Base64 formatında şifrele veya yalın veri çıktısı olarak deşifre et."
content_hash: dc0cc82dde0880eb6111fa813c9b05a6e64ddab3
last_modified_at: 2024-03-17
related_topics:
  - title: Deutsch version
    url: /de/common/base64.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/base64.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base64.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/base64.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base64.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

Bir dosya veya standart veriyi Base64 formatında şifrele veya yalın veri çıktısı olarak deşifre et.
Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/base64>.

- Bir dosyayı şifrele:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosyaismi</span>

- Bir dosyayı deşifre et:

`base64 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dosyaismi</span>

- `stdin`'den şifrele:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">herhangibirkomut</span>` | base64`

- `stdin`'den deşifre et:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">herhangibirkomut</span>` | base64 --decode`
