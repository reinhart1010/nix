---
layout: page
title: common/autoflake (polski)
description: "Usuń nieużywane importy i zmienne z kodu Python."
content_hash: 4d37eac2a5d418d6aa207b6dfc79cb96b1af4989
last_modified_at: 2024-06-14
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/autoflake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autoflake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autoflake

Usuń nieużywane importy i zmienne z kodu Python.
Więcej informacji: <https://github.com/myint/autoflake>.

- Usuń nieużywane zmienne z jednego pliku i wyświetl różnicę:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.py</span>

- Usuń nieużywane importy z wielu plików i wyświetl różnice:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku1.py ścieżka/do/pliku2.py ...</span>

- Usuń nieużywane zmienne z pliku, zastępując plik:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.py</span>

- Usuń nieużywane zmienne rekurencyjnie ze wszystkich plików w katalogu, nadpisując każdy plik:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/katalogu</span>
