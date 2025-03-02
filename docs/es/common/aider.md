---
layout: page
title: common/aider (español)
description: "Programa de emparejamiento con el LLM de su elección."
content_hash: f68fe89d1406550ed56354008bfa900ef47d1ae2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/aider.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aider

Programa de emparejamiento con el LLM de su elección.
Más información: <https://github.com/Aider-AI/aider>.

- Inicia un nuevo proyecto o trabaja con una base de código existente:

`aider --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_modelo</span>` --api-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">su_clave_api</span>

- Añade nuevas funciones o casos de prueba a archivos específicos:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Describe un error y deja que `aider` lo solucione:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` --describe "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">descripción_de_un_fallo</span>`"`

- Refactoriza código en un archivo específico:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` --refactor`

- Actualiza la documentación:

`aider `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` --update-docs`

- Muestra la ayuda:

`aider --help`
