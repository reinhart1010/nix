---
layout: page
title: common/helix (español)
description: "Helix, un editor de texto postmoderno, ofrece varios modos para diferentes tipos de manipulación de texto."
content_hash: 7626a2e87da73aa65ec6f69a45d0f9edefb3b8ff
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/common/helix.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/helix.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/helix.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/helix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/helix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># helix

Helix, un editor de texto postmoderno, ofrece varios modos para diferentes tipos de manipulación de texto.
Al presionar `i` entra en modo de inserción. `<Esc>` entra en modo normal, lo que permite el uso de comandos Helix.
Más información: <https://helix-editor.com>.

- Abre un archivo:

`helix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Abre archivos y los muestra uno al lado del otro:

`helix --vsplit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2</span>

- Muestra el tutorial para aprender Helix (o acceder al mismo dentro de Helix presionando `<Esc>` y escribiendo `:tutor`):

`helix --tutor`

- Cambia el tema (theme) de Helix:

`:theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_tema</span>

- Guarda y sale:

`:wq<Enter>`

- Sale a la fuerza sin guardar:

`:q!<Enter>`

- Deshace la última operación:

`u`

- Busca un patrón en el archivo (al presionar `n`/`N` va a la coincidencia siguiente/anterior):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_de_búsqueda</span>`<Enter>`
