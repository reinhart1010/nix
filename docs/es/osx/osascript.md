---
layout: page
title: osx/osascript (español)
description: "Ejecuta AppleScript o JavaScript for Automation (JXA) desde la línea de comandos."
content_hash: 24f37348c78980bad41ad14ce862dc8c39ba8a6d
last_modified_at: 2023-06-30
related_topics:
  - title: English version
    url: /en/osx/osascript.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/osascript.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/osascript.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># osascript

Ejecuta AppleScript o JavaScript for Automation (JXA) desde la línea de comandos.
Más información: <https://ss64.com/osx/osascript.html>.

- Ejecuta un comando AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello world'</span>`"`

- Ejecuta varios comandos AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello'</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'world'</span>`"`

- Ejecuta un archivo AppleScript compilado (`*.scpt`), empaquetado (`*.scptd`) o un archivo Applescript en texto plano (`*.applescript`):

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/apple.scpt</span>

- Obtiene el identificador del paquete de una aplicación (útil para `open -b`):

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Application</span>`"'`

- Ejecuta un comando JavaScript:

`osascript -l JavaScript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log('Hola mundo');</span>`"`

- Ejecuta un archivo JavaScript:

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.js</span>
