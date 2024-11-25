---
layout: page
title: common/radare2 (español)
description: "Un conjunto de herramientas de ingeniería inversa."
content_hash: e0694997081cd7c2058ab0482c2982ee6e54425a
last_modified_at: 2024-11-25
related_topics:
  - title: English version
    url: /en/common/radare2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/radare2.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/radare2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# radare2

Un conjunto de herramientas de ingeniería inversa.
Más información: <https://www.radare.org/r/docs.html>.

- Abre un archivo en modo escritura sin analizar los encabezados del formato de archivo:

`radare2 -nw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Depura un programa:

`radare2 -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Ejecuta un script antes de entrar en la CLI interactiva:

`radare2 -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/script.r2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/binario</span>

- Muestra texto de ayuda para cualquier comando en la CLI interactiva:

`> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">radare2_comando</span>`?`

- Ejecuta un comando desde la CLI interactiva:

`> !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_comando</span>

- Vierte los bytes crudos del bloque actual a un archivo:

`> pr > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bin</span>
