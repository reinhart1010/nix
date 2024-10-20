---
layout: page
title: common/ed (español)
description: "El editor de texto original de Unix."
content_hash: 87b5cc038e77a3af61ea4a97b9de2758f8174a1b
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/ed.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ed.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ed.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ed

El editor de texto original de Unix.
Vea también: `awk`, `sed`.
Más información: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia una sesión de editor interactivo con un documento vacío:

`ed`

- Inicia una sesión de editor interactivo con un documento vacío y un prompt específico:

`ed --prompt='> '`

- Inicia una sesión de editor interactivo con errores amigables:

`ed --verbose`

- Inicia una sesión de editor interactivo con un documento vacío y sin diagnósticos, conteos de bytes y prompt de '!':

`ed --quiet`

- Inicia una sesión de editor interactivo sin cambio de estado de salida cuando un comando falla:

`ed --loose-exit-status`

- Edita un archivo específico (esto muestra el conteo de bytes del archivo cargado):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Reemplaza una cadena con un reemplazo específico en todas las líneas:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión_regular</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reemplazo</span>`/g`
