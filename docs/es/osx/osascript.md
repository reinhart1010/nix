---
layout: page
title: osx/osascript (español)
description: "Ejecuta AppleScript o JavaScript for Automation (JXA) desde la línea de comandos."
content_hash: c0b677455a3af7a014e326bf129ae14262ed7cc3
last_modified_at: 2024-01-31
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
tldri18n_status: 2
---
# osascript

Ejecuta AppleScript o JavaScript for Automation (JXA) desde la línea de comandos.
Más información: <https://keith.github.io/xcode-man-pages/osascript.1.html>.

- Ejecuta un comando AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello world'</span>`"`

- Ejecuta varios comandos AppleScript:

`osascript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'Hello'</span>`" -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">say 'world'</span>`"`

- Ejecuta un archivo AppleScript compilado (`*.scpt`), empaquetado (`*.scptd`) o un archivo Applescript en texto plano (`*.applescript`):

`osascript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/apple.scpt</span>

- Obtén el identificador del paquete de una aplicación (útil para `open -b`):

`osascript -e 'id of app "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Application</span>`"'`

- Ejecuta un comando JavaScript:

`osascript -l JavaScript -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console.log('Hola mundo');</span>`"`

- Ejecuta un archivo JavaScript:

`osascript -l JavaScript `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.js</span>
