---
layout: page
title: common/adb-logcat (español)
description: "Vuelca un registro de mensajes del sistema."
content_hash: b60d8bddc09ce50c82166d187caf0d330ef570ca
last_modified_at: 2023-02-20
related_topics:
  - title: English version
    url: /en/common/adb-logcat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/adb-logcat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/adb-logcat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adb logcat

Vuelca un registro de mensajes del sistema.
Más información: <https://developer.android.com/studio/command-line/logcat>.

- Muestra registros del sistema:

`adb logcat`

- Muestra las líneas que coinciden con una expresión regular:

`adb logcat -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresion_regular</span>

- Muestra los registros de una etiqueta en un modo específico ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent), filtrando otras etiquetas:

`adb logcat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modo</span>` *:S`

- Muestra los registros de aplicaciones React Native en modo [V]erbose [S]ilencing otras etiquetas:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Muestra los registros de todas las etiquetas con nivel de prioridad [W]arning y superior:

`adb logcat *:W`

- Colorea el registro (normalmente se utiliza con filtros):

`adb logcat -v color`
