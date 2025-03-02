---
layout: page
title: linux/apx-stacks (español)
description: "Administra stacks en `apx`."
content_hash: 625cc0c64366f656714f3c005754999e336a2733
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/apx-stacks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/apx-stacks.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apx-stacks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx stacks

Administra stacks en `apx`.
Nota: las configuraciones de stacks creadas por el usuario se almacenan en `~/.local/share/apx/stacks`.
Más información: <https://github.com/Vanilla-OS/apx>.

- Crea de forma interactiva una nueva configuración de stack:

`apx stacks new`

- Actualiza de forma interactiva una configuración de stack:

`apx stacks update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Muestra la lista de todas las configuraciones de stacks disponibles:

`apx stacks list`

- Elimina una configuración de stack específica:

`apx stacks rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_caracteres</span>

- Importa una configuración de stack:

`apx stacks import --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/stack.yml</span>

- Exporta una configuración de stack (Nota: la opción de salida es opcional, por defecto se exporta al directorio de trabajo actual):

`apx stacks export --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_caracteres</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_salida</span>
