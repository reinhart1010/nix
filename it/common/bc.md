---
layout: page
title: common/bc (italiano)
description: "Calcolatore."
content_hash: d9a4ef3a773269324429e82054e9a90f412b3d87
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
---
# bc

Calcolatore.
Maggiori informazioni: <https://manned.org/bc>.

- Esegui in modalità interattiva utilizzando la libreria math della standard library:

`bc -l`

- Calcola il risultato di un'espressione:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcola un'espressione forzando il numero di decimali usati a 10:

`bc <<< "scale=10; 5 / 3"`

- Calcola un'espressione con seno e coseno utilizzando mathlib:

`bc -l <<< "s(1) + c(1)"`
