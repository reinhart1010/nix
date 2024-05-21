---
layout: page
title: common/gleam (español)
description: "El compilador, la herramienta de compilación, el gestor de paquetes y el formateador de código para Gleam, \"un lenguaje amigable para construir sistemas de tipo seguro escalables\"."
content_hash: 0ec207888a039ff8c50d38385b6dd734c3b84186
last_modified_at: 2024-05-21
related_topics:
  - title: English version
    url: /en/common/gleam.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gleam.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gleam

El compilador, la herramienta de compilación, el gestor de paquetes y el formateador de código para Gleam, "un lenguaje amigable para construir sistemas de tipo seguro escalables".
Más información: <https://gleam.run/writing-gleam/command-line-reference/>.

- Crea un nuevo proyecto gleam:

`gleam new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proyecto</span>

- Construye y ejecuta un proyecto gleam:

`gleam run`

- Construye el proyecto:

`gleam build`

- Ejecuta un proyecto para una plataforma y un tiempo de ejecución específico:

`gleam run --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plataforma</span>` --runtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiempo_de_ejecución</span>

- Añade una dependencia hexadecimal a tu proyecto:

`gleam add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_dependencia</span>

- Ejecuta las pruebas del proyecto:

`gleam test`

- Formatea el código fuente:

`gleam format`

- Comprueba el tipo de proyecto:

`gleam check`
