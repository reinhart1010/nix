---
layout: page
title: common/pants (español)
description: "Herramienta de flujo de trabajo rápida, escalable, fácil de usar y de código abierto."
content_hash: 0a5b7b4252fc19d6e84f5d0ee75a7bff535e2b53
last_modified_at: 2024-09-21
related_topics:
  - title: English version
    url: /en/common/pants.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pants.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pants

Herramienta de flujo de trabajo rápida, escalable, fácil de usar y de código abierto.
Más información: <https://www.pantsbuild.org/2.20/docs/using-pants/command-line-help>.

- Lista todos los objetivos:

`pants list ::`

- Ejecuta todas las pruebas:

`pants test ::`

- Arregla, formatea y limpia sólo los archivos no comprometidos:

`pants --changed-since=HEAD fix fmt lint`

- Comprueba sólo los archivos no comprometidos y sus dependientes:

`pants --changed-since=HEAD --changed-dependents=transitive check`

- Crea un paquete distribuible para el objetivo especificado:

`pants package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio:nombre-destino</span>

- Autogenera objetivos de archivo BUILD para nuevos archivos fuente:

`pants tailor ::`

- Muestra la ayuda:

`pants help`
