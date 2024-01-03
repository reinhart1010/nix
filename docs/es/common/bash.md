---
layout: page
title: common/bash (español)
description: "Bourne-Again SHell, un intérprete de línea de comandos compatible con `sh`."
content_hash: ec9ff8e53ea92c66f1d46314d618e93c9fa96c4c
last_modified_at: 2024-01-03
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bash

Bourne-Again SHell, un intérprete de línea de comandos compatible con `sh`.
Vea también: `zsh`; `histexpand`, para expansión de historial de comandos.
Más información: <https://www.gnu.org/software/bash/>.

- Inicia un intérprete de comandos interactivo:

`bash`

- Inicia el intérprete sin leer archivos de configuración:

`bash --norc`

- Ejecuta un comando:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Ejecuta comandos desde un archivo:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.sh</span>

- Ejecuta comandos desde un archivo, mostrando todos los comando ejecutados en la terminal:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.sh</span>

- Ejecuta comandos desde un archivo, deteniéndose en el primer error:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.sh</span>

- Ejecuta comandos desde `stdin` (entrada estándar):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'bash es ejecutado'"</span>` | bash`

- Inicia el intérprete [r]estringido:

`bash -r`
