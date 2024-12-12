---
layout: page
title: common/compgen (español)
description: "Un comando integrado para autocompletar en Bash, que se invoca al presionar la tecla TAB dos veces."
content_hash: 390fc9b1d0ee761febb05337e3516a56dd0a6f02
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/common/compgen.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/compgen.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/compgen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/compgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# compgen

Un comando integrado para autocompletar en Bash, que se invoca al presionar la tecla TAB dos veces.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- Lista todos los comandos que podría ejecutar:

`compgen -c`

- Lista todos los alias:

`compgen -a`

- Lista todas las funciones que podría ejecutar:

`compgen -A function`

- Muestra palabras reservadas de la interfaz de comandos (shell):

`compgen -k`

- Muestra todos los comandos/alias disponibles comenzando con 'ls':

`compgen -ac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>
