---
layout: page
title: common/ls (polski)
description: "Wypisz zawartość katalogu."
content_hash: 4c9d690f5742f1d28f97d981da8835cc81c01237
last_modified_at: 2023-11-01
related_topics:
  - title: català version
    url: /ca/common/ls.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ls.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/ls.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ls.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ls.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ls

Wypisz zawartość katalogu.
Więcej informacji: <https://www.gnu.org/software/coreutils/ls>.

- Wypisz po jednym pliku w linijce:

`ls -1`

- Wypisz wszystkie pliki, w tym ukryte:

`ls -a`

- Wypisz wszystkie pliki z `/` na końcu nazw katalogów:

`ls -F`

- Lista w długim formacie (uprawnienia, właściciel/ka, rozmiar i data modyfikacji) wszystkich plików:

`ls -la`

- Lista w długim formacie z rozmiarem w jednostkach z przedrostkami dwójkowymi (KiB, MiB, GiB):

`ls -lh`

- Lista w długim formacie posortowana rozmiarem (malejąco):

`ls -lS`

- Lista wszystkich plików w długim formacie posortowanych według daty modyfikacji (od najstarszych):

`ls -ltr`

- Wypisz tylko katalogi:

`ls -d */`
