---
layout: page
title: common/difft (español)
description: "Compara archivos o directorios en base de la sintaxis del lenguaje de programación."
content_hash: e92437d349207d2ccbafec10f1d68befa84fdfda
last_modified_at: 2024-04-18
related_topics:
  - title: English version
    url: /en/common/difft.html
    icon: bi bi-globe
tldri18n_status: 2
---
# difft

Compara archivos o directorios en base de la sintaxis del lenguaje de programación.
Vea también: `delta`, `diff`.
Más información: <https://difftastic.wilfred.me.uk/introduction.html>.

- Compara dos archivos o directorios:

`difft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio2</span>

- Informa únicamente diferencias entre los archivos:

`difft --check-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Especifica el modo de visualización (por defecto es `side-by-side`):

`difft --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">side-by-side|side-by-side-show-both|inline|json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Ignora comentarios al comparar:

`difft --ignore-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Activa o desactiva el resaltado sintáctico del código fuente (por defecto está activado):

`difft --syntax-highlight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Silenciosamente omite los archivos que no hayan cambiado:

`difft --skip-unchanged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_o_directorio2</span>

- Lista todos los lenguajes de programación soportados por la herramienta, junto con sus extensiones:

`difft --list-languages`
