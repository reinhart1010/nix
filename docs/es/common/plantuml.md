---
layout: page
title: common/plantuml (español)
description: "Crea diagramas UML a partir de un lenguaje de texto plano y los renderiza en diferentes formatos."
content_hash: c55417c49179005d3b7b6e99a6f932df051bb59e
last_modified_at: 2024-09-27
related_topics:
  - title: Deutsch version
    url: /de/common/plantuml.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/plantuml.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/plantuml.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># plantuml

Crea diagramas UML a partir de un lenguaje de texto plano y los renderiza en diferentes formatos.
Más información: <https://plantuml.com/en/command-line>.

- Renderiza los diagramas al formato por defecto (PNG):

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama1.puml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama2.puml</span>

- Renderiza un diagrama en un formato determinado (p.ej. `png`, `pdf`, `svg`, `txt`):

`plantuml -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formato</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama.puml</span>

- Renderiza todos los diagramas de un directorio:

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/diagramas</span>

- Renderiza un diagrama al directorio de salida:

`plantuml -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/salida</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama.puml</span>

- Renderiza un diagrama sin almacenar el código fuente del diagrama (Nota: Se almacena por defecto cuando no se especifica la opción `-nometadata`):

`plantuml -nometadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama.puml</span>

- Recupera la fuente de los metadatos de un diagrama `plantuml`:

`plantuml -metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama.png</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama.puml</span>

- Renderiza un diagrama con el archivo de configuración:

`plantuml -config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config.cfg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">diagrama.puml</span>

- Muestra la ayuda:

`plantuml -help`
