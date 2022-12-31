---
layout: page
title: common/ajson (español)
description: "Ejecuta JSONPath en objetos JSON."
content_hash: 6046b9f3f7ceb92cbe56b92e802cb8978aa88a4b
last_modified_at: 2022-12-31
related_topics:
  - title: English version
    url: /en/common/ajson.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ajson.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ajson

Ejecuta JSONPath en objetos JSON.
Más información: <https://github.com/spyzhov/ajson>.

- Lee JSON de un archivo y ejecuta una expresión JSONPath especificada:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.json</span>

- Lee JSON de `stdin` y ejecuta una expresión JSONPath especificada:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.json</span>` | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`'`

- Lee JSON de una URL y evalúa una expresión JSONPath especificada:

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avg($..price)</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ejemplo.com/api/</span>`'`

- Lee un simple cadena JSON y calcula un valor:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`' | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2 * pi * $</span>`'`
