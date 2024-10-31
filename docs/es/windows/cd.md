---
layout: page
title: windows/cd (español)
description: "Muestra el directorio de trabajo actual o se desplaza a un directorio diferente."
content_hash: e1483f7f780a477ac2901caffb8d8fa4af239a67
last_modified_at: 2024-10-31
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cd

Muestra el directorio de trabajo actual o se desplaza a un directorio diferente.
En PowerShell, este comando es un alias de `Set-Location`. Esta documentación está basada en la versión del símbolo del sistema (`cmd`) de `cd`.
Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Vea la documentación del comando PowerShell equivalente:

`tldr set-location`

- Muestra la ruta del directorio actual:

`cd`

- Va a un directorio específico en la misma unidad:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\directorio</span>

- Va a un directorio específico en una uni[d]ad diferente:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\directorio</span>

- Sube al directorio padre del directorio actual:

`cd ..`

- Va al directorio principal del usuario actual:

`cd %userprofile%`

- Va a la raíz de la unidad actual:

`cd \`
