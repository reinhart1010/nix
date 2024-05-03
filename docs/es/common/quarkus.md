---
layout: page
title: common/quarkus (español)
description: "Crea proyectos Quarkus, gestiona extensiones y realiza tareas esenciales de compilación y desarrollo."
content_hash: 8b68db8548ba895f8343f532e91b5417b988c105
last_modified_at: 2024-05-03
related_topics:
  - title: English version
    url: /en/common/quarkus.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/quarkus.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># quarkus

Crea proyectos Quarkus, gestiona extensiones y realiza tareas esenciales de compilación y desarrollo.
Más información: <https://quarkus.io/guides/cli-tooling>.

- Crea un nuevo proyecto de aplicación en un directorio nuevo:

`quarkus create app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proyecto</span>

- Ejecuta el proyecto actual en el modo de codificación en vivo:

`quarkus dev`

- Ejecuta la aplicación:

`quarkus run`

- Ejecuta el proyecto actual en modo de prueba continua:

`quarkus test`

- Añade una o más extensiones al proyecto actual:

`quarkus extension add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_extensión1 nombre_extensión2 ...</span>

- Construye un contenedor de imagen utilizando Docker:

`quarkus image build docker`

- Despliega la aplicación en Kubernetes:

`quarkus deploy kubernetes`

- Actualiza el proyecto:

`quarkus update`
