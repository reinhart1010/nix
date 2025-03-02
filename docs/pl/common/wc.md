---
layout: page
title: common/wc (polski)
description: "Zlicza linie, słowa, i bajty."
content_hash: 478c436cfec751551b31831369b6a1f79cc0faa5
last_modified_at: 2025-03-02
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
  - title: Nederlands version
    url: /nl/common/wc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Zlicza linie, słowa, i bajty.
Więcej informacji: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Policz linie w pliku:

`wc --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Policz słowa w pliku:

`wc --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Policz znaki (bajty) w pliku:

`wc --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Policz znaki w pliku (uwzględniając znaki zapisane więcej niż jednym bajtem):

`wc --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>

- Użyj standardowego wejścia aby policzyć po kolei linie, słowa, i znaki (bajty):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`

- Policz długość najdłuższej linii w pliku:

`wc --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plik</span>
