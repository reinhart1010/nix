---
layout: page
title: common/7za (polski)
description: "Archiwizator plików o wysokim współczynniku kompresji."
content_hash: 2ec58edb95671bbcf17e2e6356c65bc469316caa
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/7za.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7za.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7za.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7za.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7za.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7za.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/7za.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7za.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7za.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7za.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7za.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/7za.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7za.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7za.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7za.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7za.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># 7za

Archiwizator plików o wysokim współczynniku kompresji.
Samodzielna wersja `7z` z obsługą mniejszej liczby typów archiwów.
Więcej informacji: <https://manned.org/7za>.

- Zarchiwizuj plik lub katalog:

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/pliku_lub_katalogu</span>

- Wyodrębnij istniejący plik 7z z oryginalną strukturą katalogów:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum</span>

- Zarchiwizuj przy użyciu określonego typu archiwum:

`7za a -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zip|gzip|bzip2|tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scieżka/do/pliku_lub_katalogu</span>

- Wypisz dostępe typy archiwów:

`7za i`

- Wypisz zawartość pliku archiwum:

`7za l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archiwum</span>
