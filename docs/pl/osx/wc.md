---
layout: page
title: osx/wc (polski)
description: "Zlicza linie, słowa, i bajty."
content_hash: 14f7c49ea14ae9e464f76c958110a0fee9b701d4
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/wc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Zlicza linie, słowa, i bajty.
Więcej informacji: <https://keith.github.io/xcode-man-pages/wc.1.html>.

- Policz linie w pliku:

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Policz słowa w pliku:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Policz znaki (bajty) w pliku:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Policz znaki w pliku (uwzględniając znaki zapisane więcej niż jednym bajtem):

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Użyj standardowego wejścia aby policzyć po kolei linie, słowa, i znaki (bajty):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
