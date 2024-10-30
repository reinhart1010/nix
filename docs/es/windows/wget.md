---
layout: page
title: windows/wget (español)
description: "En PowerShell, este comando puede ser un alias de `Invoke-WebRequest` cuando el programa original `wget` (<https://www.gnu.org/software/wget>) no está correctamente instalado."
content_hash: c083eeeb482ca600eac11e044e2cbf9688b7906e
last_modified_at: 2024-10-30
related_topics:
  - title: বাংলা version
    url: /bn/windows/wget.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/wget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/wget.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/wget.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/wget.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/wget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/wget.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/wget.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wget

En PowerShell, este comando puede ser un alias de `Invoke-WebRequest` cuando el programa original `wget` (<https://www.gnu.org/software/wget>) no está correctamente instalado.
Nota: si el comando version devuelve un error, PowerShell puede haber sustituido este comando por `Invoke-WebRequest`.
Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Vea la documentación del comando original `wget`:

`tldr wget -p common`

- Vea la documentación del comando `Invoke-WebRequest` de PowerShell:

`tldr invoke-webrequest`

- Muestra versión:

`wget --version`
