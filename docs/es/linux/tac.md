---
layout: page
title: linux/tac (español)
description: "Muestra y concatena archivos con las líneas en orden inverso."
content_hash: eb5712b8ecd6a8f8e19b14a889bc39abc3203b8c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/tac.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/tac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/tac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tac

Muestra y concatena archivos con las líneas en orden inverso.
Vea también: `cat`.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- Concatena archivos específicos en orden inverso:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Muestra `stdin` en orden inverso:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat ruta/al/archivo</span>` | tac`

- Usa un separador específico:

`tac --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Usa una expresión regular específica como separador:

`tac --regex --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[,;]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Usa un separador antes de cada archivo:

`tac --before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>
