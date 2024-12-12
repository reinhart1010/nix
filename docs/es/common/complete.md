---
layout: page
title: common/complete (español)
description: "Autocompleta argumentos para comandos de la interfaz interactiva (shell)."
content_hash: 452351c24a8d43080ddb0c310b08a33950833172
last_modified_at: 2024-12-12
related_topics:
  - title: English version
    url: /en/common/complete.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/complete.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/complete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# complete

Autocompleta argumentos para comandos de la interfaz interactiva (shell).
Más información: <https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion-Builtins.html>.

- Aplica una función que realiza autocompletado a un comando:

`complete -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">función</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Aplica un comando que realiza autocompletado a otro comando:

`complete -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_de_autocompletado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Aplica autocompletado sin agregar espacio a la palabra completada:

`complete -o nospace -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">función</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
