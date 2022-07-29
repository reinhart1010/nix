---
layout: page
title: common/bc (italiano)
description: "Calcolatore."
content_hash: 79d7b93146d8c8791f27a5a9e5894a541210be36
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

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bc

Calcolatore.
Maggiori informazioni: <https://manned.org/man/bc.1>.

- Esegui in modalità interattiva utilizzando la libreria math della standard library:

`bc -l`

- Calcola il risultato di un'espressione:

`bc <<< "(1 + 2) * 2 ^ 2"`

- Calcola un'espressione forzando il numero di decimali usati a 10:

`bc <<< "scale=10; 5 / 3"`

- Calcola un'espressione con seno e coseno utilizzando mathlib:

`bc -l <<< "s(1) + c(1)"`
