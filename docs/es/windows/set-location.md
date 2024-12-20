---
layout: page
title: windows/set-location (español)
description: "Muestra el directorio de trabajo actual o va a un directorio diferente."
content_hash: ba8b636711d1adbe4e98838c854e959edc460adb
last_modified_at: 2024-12-20
related_topics:
  - title: English version
    url: /en/windows/set-location.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/set-location.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/set-location.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/set-location.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Set-Location

Muestra el directorio de trabajo actual o va a un directorio diferente.
Nota: Este comando sólo se puede utilizar a través de PowerShell.
Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Va al directorio especificado:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\directorio</span>

- Va a un directorio específico en una unidad diferente:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\directorio</span>

- Va y muestra la ubicación del directorio especificado:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\directorio</span>` -PassThru`

- Sube al padre del directorio actual:

`Set-Location ..`

- Va al directorio principal del usuario actual:

`Set-Location ~`

- Regresa/va al directorio elegido anteriormente:

`Set-Location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-|+</span>

- Va a la raíz de la unidad actual:

`Set-Location \`
