---
layout: page
title: common/figlet (español)
description: "Genera encabezados usando caracteres ASCII desde la entrada del usuario."
content_hash: f8a9af912de2363eb34cc5673b0a684358cdc3db
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/figlet.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># figlet

Genera encabezados usando caracteres ASCII desde la entrada del usuario.
Véase también `showfigfonts`.
Más información: <http://www.figlet.org/figlet-man.html>.

- Genera el encabezado directamente introduciendo el texto:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_entrada</span>

- Usa un archivo de fuente personalizada:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_entrada</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_fuente.flf</span>

- Use una fuente del directorio predeterminado (la extensión puede ser omitida):

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_entrada</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_fuente</span>

- Redirige la salida de un comando hacia figlet:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | figlet`
