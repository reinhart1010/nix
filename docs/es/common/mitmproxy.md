---
layout: page
title: common/mitmproxy (español)
description: "Un proxy HTTP interactivo man-in-the-middle."
content_hash: 594f70e509e2073667807bc113c99c4185740637
last_modified_at: 2024-09-04
related_topics:
  - title: English version
    url: /en/common/mitmproxy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mitmproxy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mitmproxy

Un proxy HTTP interactivo man-in-the-middle.
Vea también: `mitmweb` y `mitmdump`.
Más información: <https://docs.mitmproxy.org/stable/>.

- Inicia `mitmproxy` con la configuración por defecto (escuchará en el puerto `8080`):

`mitmproxy`

- Inicia `mitmproxy` con una dirección y puerto personalizados:

`mitmproxy --listen-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--listen-port|-p</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Inicia `mitmproxy` utilizando un script para procesar el tráfico:

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--scripts|-s</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/script.py</span>

- Exporta los registros con las claves maestras SSL/TLS a programas externos (wireshark, etc.):

`SSLKEYLOGFILE="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>`" mitmproxy`

- Especifica el modo de funcionamiento del servidor proxy (`regular` es el predeterminado):

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--mode|-m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular|transparent|socks5|...</span>

- Configura el diseño de la consola:

`mitmproxy --console-layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horizontal|single|vertical</span>
