---
layout: page
title: common/typeinc (español)
description: "Un programa de línea de comandos basado en `ncurses` para probar la velocidad de tecleo, escrito en Python."
content_hash: 9f1925ab5f5d8c812e3bcee6943c933dc68d3f0c
last_modified_at: 2024-06-09
related_topics:
  - title: English version
    url: /en/common/typeinc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/typeinc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># typeinc

Un programa de línea de comandos basado en `ncurses` para probar la velocidad de tecleo, escrito en Python.
Prueba diferentes niveles de dificultad y mejora tu velocidad de tecleo.
Más información: <https://github.com/AnirudhG07/Typeinc>.

- Entra en la prueba de mecanografía:

`typeinc`

- Muestra la lista de los 10 primeros clasificados por nivel de dificultad de entrada::

`typeinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--ranklist</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nivel_de_dificultad</span>

- Obtén palabras aleatorias en inglés presentes en nuestra lista de palabras:

`typeinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-w|--words</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">conteo_de_palabras</span>

- Calcula el resultado hipotético en Typeinc:

`typeinc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--score</span>
