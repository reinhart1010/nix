---
layout: page
title: common/nnn (español)
description: "Gestor de archivos de terminal interactivo y analizador de uso de disco."
content_hash: c6447434ee59503ca3d4f5b7923c4f81d1b7bf76
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/nnn.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nnn

Gestor de archivos de terminal interactivo y analizador de uso de disco.
Vea también: `clifm`, `mc`, `ranger`, `vifm`.
Más información: <https://github.com/jarun/nnn>.

- Abre el directorio actual (o especifica uno como primer argumento):

`nnn`

- Inicia en modo detallado:

`nnn -d`

- Muestra archivos ocultos:

`nnn -H`

- Abre un marcador existente (definido en la variable de entorno `NNN_BMS`):

`nnn -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_marcador</span>

- Ordena los archivos por [a]parente uso de disco / uso de [d]isco / [e]xtensión / inve[r]so / tamaño / [t]iempo / [v]ersión:

`nnn -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|d|e|r|s|t|v</span>

- Abre archivos que elijas. Selecciona un archivo y oprime `o`, después escribe el nombre del programa con el cual abrirlo:

`nnn -o`
