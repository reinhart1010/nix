---
layout: page
title: common/tuc (español)
description: "Corta texto (o bytes) donde coincida un delimitador, luego conserva las partes deseadas."
content_hash: 4a5903992515693128fdf8908738f6ea1066c27d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tuc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tuc

Corta texto (o bytes) donde coincida un delimitador, luego conserva las partes deseadas.
Una versión más fácil de usar y potente de `cut` con valores por defecto sensibles.
Más información: <https://github.com/riquito/tuc>.

- Corta y reorganiza campos:

`echo "foo bar baz" | tuc -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> </span>`' -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,2,1</span>

- Sustituye el delimitador `space` por una flecha:

`echo "foo bar baz" | tuc -d ' ' -r ' ➡ '`

- Mantiene un rango de campos:

`echo "foo bar baz" | tuc -d ' ' -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2:</span>

- Corta usando expresiones regulares:

`echo "a,b, c" | tuc -e '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[, ]+</span>`' -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>

- Genera salida JSON:

`echo "foo bar baz" | tuc -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> </span>`' --json`
