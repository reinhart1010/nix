---
layout: page
title: windows/curl (español)
description: "En PowerShell, este comando puede ser un alias de `Invoke-WebRequest` cuando el programa original `curl` (<https://curl.se>) no está correctamente instalado."
content_hash: 16f3a0c781f91757e9f8c130cf21780b2b52a5de
last_modified_at: 2024-10-20
related_topics:
  - title: বাংলা version
    url: /bn/windows/curl.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/curl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/curl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/curl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/curl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/curl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/curl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># curl

En PowerShell, este comando puede ser un alias de `Invoke-WebRequest` cuando el programa original `curl` (<https://curl.se>) no está correctamente instalado.
Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Consulta la documentación del comando original `curl`:

`tldr curl -p common`

- Vea la documentación del comando `Invoke-WebRequest` de PowerShell:

`tldr invoke-webrequest`

- Comprueba si `curl` está correctamente instalado imprimiendo su número de versión. Si este comando da error, PowerShell puede haber sustituido este comando por `Invoke-WebRequest`:

`curl --version`
