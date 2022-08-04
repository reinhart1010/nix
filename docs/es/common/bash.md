---
layout: page
title: common/bash (español)
description: "Bourne-Again SHell."
content_hash: e770046740e41be8c7c25e34930edfe4a498a307
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
---
# bash

Bourne-Again SHell.
Intérprete de línea de comandos compatible con `sh`.
Más información: <https://gnu.org/software/bash/>.

- Inicia un intérprete de comandos interactivo:

`bash`

- Ejecuta un comando:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Ejecuta comandos desde un archivo:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.sh</span>

- Ejecuta comandos desde un archivo, mostrando todos los comando ejecutados en la terminal:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.sh</span>

- Ejecuta comandos desde un archivo, deteniéndose en el primer error:

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.sh</span>

- Ejecuta comandos desde stdin (entrada estándar):

`bash -s`

- Imprime la información de la versión de bash (use `echo $BASH_VERSION` para ver sólo la versión sin la información sobre la licencia):

`bash --version`
