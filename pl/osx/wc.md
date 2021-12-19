---
layout: page
title: osx/wc (polski)
description: "Zlicza linie, słowa, i bajty"
content_hash: 37283e7d0261a3e8417327dbc249f66997a143bf
related_topics:
  - title: English version
    url: /en/osx/wc.html
    icon: bi bi-globe
---
# wc

Zlicza linie, słowa, i bajty
Więcej informacji: <https://www.gnu.org/software/coreutils/wc>.

- Policz linie w pliku

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Policz słowa w pliku:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Policz znaki (bajty) w pliku:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Policz znaki w pliku (uwzględniając znaki zapisane więcej niż jednym bajtem):

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Użyj standardowego wejścia aby policzyć po kolei linie, słowa, i znaki (bajty):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
