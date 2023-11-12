---
layout: page
title: common/wc (polski)
description: "Zlicza linie, słowa, i bajty."
content_hash: 6207bd0f4733f885258a1600a319b017c072a5f0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/wc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/wc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/wc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/wc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Zlicza linie, słowa, i bajty.
Więcej informacji: <https://www.gnu.org/software/coreutils/wc>.

- Policz linie w pliku:

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Policz słowa w pliku:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Policz znaki (bajty) w pliku:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Policz znaki w pliku (uwzględniając znaki zapisane więcej niż jednym bajtem):

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Użyj standardowego wejścia aby policzyć po kolei linie, słowa, i znaki (bajty):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`

- Policz długość najdłuższej linii w pliku:

`wc --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>
