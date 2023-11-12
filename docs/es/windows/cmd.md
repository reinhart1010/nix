---
layout: page
title: windows/cmd (español)
description: "El intérprete de comandos de Windows."
content_hash: f443d32bbddac1f3cf580a532c7d7e0d15734ed0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/cmd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cmd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cmd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cmd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cmd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cmd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmd.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/cmd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmd

El intérprete de comandos de Windows.
Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Inicia una sesión shell interactiva:

`cmd`

- Ejecuta [c]omandos específicos:

`cmd /c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hola Mundo</span>

- Ejecuta un script específico:

`cmd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\script.bat</span>

- Ejecuta comandos específicos y luego entrar en un shell interactivo:

`cmd /k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo Hola Mundo</span>

- Inicia una sesión shell interactiva donde `echo` está desactivado en la salida de comandos:

`cmd /q`

- Inicia una sesión de shell interactiva con la expansión [v]ariable retardada activada o desactivada:

`cmd /v:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Inicia una sesión shell interactiva con [e]xtensiones de comando activadas o desactivadas:

`cmd /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Inicia una sesión shell interactiva with con la codificación [u]nicode utilizada:

`cmd /u`
