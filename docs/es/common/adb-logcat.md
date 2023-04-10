---
layout: page
title: common/adb-logcat (español)
description: "Vuelca un registro de mensajes del sistema."
content_hash: 8573be2ca9936fd8873d9e48b48d019a32f373da
last_modified_at: 2023-04-10
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
# adb logcat

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

- Muestra los registros de un proceso específico:

`adb logcat --pid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Muestra los registros del proceso de un paquete específico:

`adb logcat --pid=$(adb shell pidof -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>`)`

- Colorea el registro (normalmente se utiliza con filtros):

`adb logcat -v color`
