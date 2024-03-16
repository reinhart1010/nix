---
layout: page
title: common/figlet (español)
description: "Genera encabezados usando caracteres ASCII desde la entrada del usuario."
content_hash: 469467b625abe57603243aa28aa43dbb8f180b6d
last_modified_at: 2024-03-16
related_topics:
  - title: English version
    url: /en/common/figlet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# figlet

Genera encabezados usando caracteres ASCII desde la entrada del usuario.
Véase también `showfigfonts`.
Más información: <http://www.figlet.org/figlet-man.html>.

- Genera el encabezado directamente introduciendo el texto:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_entrada</span>

- Usa un archivo de [f]uente personalizada:

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_entrada</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_fuente.flf</span>

- Usa una [f]uente del directorio predeterminado (la extensión puede ser omitida):

`figlet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_entrada</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_fuente</span>

- Redirige la salida de un comando hacia FIGlet:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` | figlet`

- Muestra las fuentes de FIGlet disponibles:

`showfigfonts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_opcional_para_mostrar</span>

- Utiliza el ancho total del [t]erminal y [c]entra el texto de entrada:

`figlet -t -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_entrada</span>

- Muestra todos los caracteres utilizando todo su ancho para evitar traslapes:

`figlet -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_text</span>
