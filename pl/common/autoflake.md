---
layout: page
title: common/autoflake (polski)
description: "Narzędzie do usuwania nieużywanych importów i zmiennych z kodu Python."
content_hash: b0269ef470f50098ce0ad4e44ef67126a6c6a2e9
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
---
# autoflake

Narzędzie do usuwania nieużywanych importów i zmiennych z kodu Python.
Więcej informacji: <https://github.com/myint/autoflake>.

- Usuń nieużywane zmienne z jednego pliku i wyświetl różnicę:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Usuń nieużywane importy z wielu plików i wyświetl różnice:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3.py</span>

- Usuń nieużywane zmienne z pliku, zastępując plik:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Usuń nieużywane zmienne rekurencyjnie ze wszystkich plików w katalogu, nadpisując każdy plik:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/katalogu</span>
