---
layout: page
title: common/wafw00f (español)
description: "Identifica y toma las huellas digitales de los productos Web Application Firewall (WAF) que protegen un sitio web."
content_hash: dd57114dc5ec8f1b647c14ae258ec47a3ee910b6
last_modified_at: 2024-07-07
related_topics:
  - title: English version
    url: /en/common/wafw00f.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wafw00f.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wafw00f

Identifica y toma las huellas digitales de los productos Web Application Firewall (WAF) que protegen un sitio web.
Más información: <https://github.com/EnableSecurity/wafw00f>.

- Comprueba si un sitio web utiliza algún WAF:

`wafw00f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.ejemplo.com</span>

- Comprueba a todos los WAF detectables sin detenerse en la primera coincidencia:

`wafw00f --findall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.ejemplo.com</span>

- Pasa peticiones a través de un [p]roxy (como BurpSuite):

`wafw00f --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://localhost:8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.ejemplo.com</span>

- [t]estea un producto WAF específico (ejecuta `wafw00f -l` para obtener una lista de todos los WAF compatibles):

`wafw00f --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Cloudflare|Cloudfront|Fastly|ZScaler|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.ejemplo.com</span>

- Pasa cabeceras personalizadas desde un archivo:

`wafw00f --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/cabeceras.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.ejemplo.com</span>

- Lee entradas de destino desde un archivo y muestra una salida detallada (múltiples `v` para más verbosidad):

`wafw00f --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/urls.txt</span>` -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v</span>

- [l]ista todos los WAF que pueden detectarse:

`wafw00f --list`
