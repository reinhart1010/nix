---
layout: page
title: windows/invoke-webrequest (español)
description: "Realiza una solicitud HTTP/HTTPS a la Web."
content_hash: 981062d66cd68a89be3ed3635b0256b0290fe8f1
last_modified_at: 2024-12-26
related_topics:
  - title: English version
    url: /en/windows/invoke-webrequest.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/invoke-webrequest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/invoke-webrequest.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/invoke-webrequest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/invoke-webrequest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Invoke-WebRequest

Realiza una solicitud HTTP/HTTPS a la Web.
Nota: Este comando solo se puede utilizar a través de PowerShell.
Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Descarga el contenido de una URL a un archivo:

`Invoke-WebRequest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -OutFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\archivo</span>

- Envía datos codificados para formularios (solicitud POST de tipo `application/x-www-form-urlencoded`):

`Invoke-WebRequest -Method Post -Body @{ name='roberto' } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/form</span>

- Envía una solicitud con un encabezado adicional, utilizando un método HTTP personalizado:

`Invoke-WebRequest -Headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@{ X-My-Header = '123' }</span>` -Method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Envía datos en formato JSON, especificando el encabezado tipo de contenido (content-type) adecuado:

`Invoke-WebRequest -Body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>` -ContentType 'application/json' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/users/1234</span>

- Pasa un nombre de usuario y contraseña para autenticación ante el servidor:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
