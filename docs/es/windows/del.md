---
layout: page
title: windows/del (español)
description: "Elimina uno o más archivos."
content_hash: 28b45a198769c19d80fb47ec6320364eede094fa
last_modified_at: 2024-01-07
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 2
---
# del

Elimina uno o más archivos.
En PowerShell, este comando es un alias de `Remove-Item`. Esta documentación se basa en la versión del símbolo del sistema (`cmd`) de `del`.
Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Muestra la documentación del comando PowerShell equivalente:

`tldr remove-item`

- Elimina uno o más archivos o patrones separados por espacios:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>

- Solicita confirmación antes de borrar cada archivo:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /p`

- Fuerza la eliminación de archivos de sólo lectura:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /f`

- Elimina recursivamente archivos de todos los subdirectorios:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /s`

- Elimina archivos que coincidan con un comodín sin confirmación:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /q`

- Muestra la ayuda y la lista de atributos disponibles:

`del /?`

- Elimina archivos en función de los atributos especificados:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atributo</span>
