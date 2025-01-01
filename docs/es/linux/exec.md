---
layout: page
title: linux/exec (español)
description: "Ejecuta un comando sin crear un proceso hijo."
content_hash: 3aab8308dfc3b460c3d97de7657810ad140947dd
last_modified_at: 2025-01-01
related_topics:
  - title: English version
    url: /en/linux/exec.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/exec.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/exec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# exec

Ejecuta un comando sin crear un proceso hijo.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- Ejecuta un comando específico:

`exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -opciones</span>

- Ejecuta un comando con un entorno (en su mayoría) vacío:

`exec -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -opciones</span>

- Ejecuta un comando como un shell de inicio de sesión:

`exec -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -opciones</span>

- Ejecuta un comando con un nombre diferente:

`exec -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando -con -opciones</span>
