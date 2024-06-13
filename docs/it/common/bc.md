---
layout: page
title: common/bc (italiano)
description: "Calcolatore."
content_hash: 2289603a348d90805694ed831cc73afd4579aec8
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bc.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bc

Calcolatore.
Maggiori informazioni: <https://manned.org/bc.1>.

- Esegui in modalità interattiva utilizzando la libreria math della standard library:

`bc -l`

- Calcola il risultato di un'espressione:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcola un'espressione forzando il numero di decimali usati a 10:

`bc <<< "scale=10; 5 / 3"`

- Calcola un'espressione con seno e coseno utilizzando mathlib:

`bc -l <<< "s(1) + c(1)"`
