---
layout: page
title: windows/remove-item (español)
description: "Elimina archivos, carpetas, así como claves de registro y subclaves."
content_hash: 09944e39019076f133edf4f311d68d811d6ee9e6
last_modified_at: 2024-12-19
related_topics:
  - title: English version
    url: /en/windows/remove-item.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/remove-item.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/remove-item.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/remove-item.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Remove-Item

Elimina archivos, carpetas, así como claves de registro y subclaves.
Este comando solo se puede ejecutar a través de PowerShell.
Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- Elimina archivos específicos o claves de registro (sin subclaves):

`Remove-Item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\archivo_o_clave1 , ruta\al\archivo_o_clave2 ...</span>

- Elimina archivos ocultos o de solo lectura:

`Remove-Item -Force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\archivo1 , ruta\al\archivo2 ...</span>

- Elimina archivos específicos o claves de registro de forma interactiva antes de cada eliminación:

`Remove-Item -Confirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\archivo_o_clave1 , ruta\al\archivo_o_clave2 ...</span>

- Elimina archivos y directorios específicos recursivamente (Windows 10 versión 1909 o posterior):

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\archivo_o_directorio1 , ruta\al\archivo_o_directorio2 ...</span>

- Quita claves específicas del registro de Windows y todas sus subclaves:

`Remove-Item -Recurse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\a\la\clave1 , ruta\a\la\clave2 ...</span>

- Realiza una simulación del proceso de eliminación:

`Remove-Item -WhatIf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\archivo1 , ruta\al\archivo2 ...</span>
