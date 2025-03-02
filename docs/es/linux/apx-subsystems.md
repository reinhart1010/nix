---
layout: page
title: linux/apx-subsystems (español)
description: "Administra subsistemas en `apx`."
content_hash: 193b0f07d20881e805f4953f70c9a0877b3dd45b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/apx-subsystems.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/apx-subsystems.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apx-subsystems.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx subsystems

Administra subsistemas en `apx`.
Los subsistemas son contenedores que pueden crearse a partir de stacks preexistentes.
Más información: <https://github.com/Vanilla-OS/apx>.

- Crea de forma interactiva un nuevo subsistema:

`apx subsystems new`

- Muestra la lista de todos los subsistemas disponibles:

`apx subsystems list`

- Restablece un subsistema específico a su estado inicial:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_caracteres</span>

- Fuerza el restablecimiento de un subsistema específico:

`apx subsystems reset --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_caracteres</span>` --force`

- Elimina un subsistema específico:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_caracteres</span>

- Fuerza la eliminación de un subsistema específico:

`apx subsystems rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_caracteres</span>` --force`
