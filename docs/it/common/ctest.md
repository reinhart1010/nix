---
layout: page
title: common/ctest (italiano)
description: "Programma per eseguire test in progetti CMake."
content_hash: e919e46badcc1ae4307662f25f5d3d5830173300
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ctest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ctest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ctest

Programma per eseguire test in progetti CMake.
Maggiori informazioni: <https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest>.

- Esegui tutti i test definiti nel progetto CMakw, eseguendo 4 job allo stesso tempo in parallelo:

`ctest -j`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --output-on-failure`

- Mostra una lista dei test disponibili:

`ctest -N`

- Esegui un singolo test in base al suo nome, o filtrando con una espressione regolare:

`ctest --output-on-failure -R '^`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_test</span>`$'`
