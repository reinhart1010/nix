---
layout: page
title: osx/ed (español)
description: "El editor de texto original de Unix."
content_hash: adb6b3e84cc0c2e730e6aa9ce97b0e69f213e308
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/ed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ed.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/osx/ed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ed

El editor de texto original de Unix.
Ver también: `awk`, `sed`.
Más información: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Inicia una sesión de edición interactiva con un documento vacío:

`ed`

- Inicia una sesión de editor interactivo con un documento vacío y un [p]rompt específico:

`ed -p '> '`

- Inicia una sesión de editor interactivo con un documento vacío y sin diagnósticos, recuento de bytes y prompt '!':

`ed -s`

- Edita un archivo específico (muestra el recuento de bytes del archivo cargado):

`ed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Reemplaza una cadena con un reemplazo específico para todas las líneas:

`,s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión_regular</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reemplazo</span>`/g`
