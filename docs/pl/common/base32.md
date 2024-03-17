---
layout: page
title: common/base32 (polski)
description: "Enkoduj lub dekoduj plik lub standardowe wejście do/z Base32, na standardowe wyjście."
content_hash: ddaa7baf8d2e4f26557274013e55ad9e2ecd9eb6
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
  - title: português (Brasil) version
    url: /pt_BR/common/base32.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/base32.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base32.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base32

Enkoduj lub dekoduj plik lub standardowe wejście do/z Base32, na standardowe wyjście.
Więcej informacji: <https://www.gnu.org/software/coreutils/base32>.

- Enkoduj plik:

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Dekoduj plik:

`base32 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwapliku</span>

- Enkoduj z `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jakiespolecenie</span>` | base32`

- Dekoduj z `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jakiespolecenie</span>` | base32 --decode`
