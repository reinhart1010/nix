---
layout: page
title: windows/del (español)
description: "Elimina uno o más archivos."
content_hash: 4654f7cef35f0d03cf5ff56664d08394f860437a
last_modified_at: 2023-10-28
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
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
---
# del

Elimina uno o más archivos.
En PowerShell, este comando es un alias de `Remove-Item`. Esta documentación se basa en la versión del símbolo del sistema (`cmd`) de `del`.
Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Ver la documentación del comando PowerShell equivalente:

`tldr remove-item`

- Elimina uno o más archivos o patrones separados por espacios:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>

- Solicita confirmación antes de borrar cada archivo:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /p`

- Fuerza la eliminación de archivos de sólo lectura:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /f`

- Eliminar de forma recursiva archivos de todos los subdirectorios:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /s`

- No generar una solicitud de confirmación al eliminar archivos basados en un comodín global:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /q`

- Muestra la ayuda y la lista de atributos disponibles:

`del /?`

- Elimina archivos en función de los atributos especificados:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patrón_del_archivo</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atributo</span>
