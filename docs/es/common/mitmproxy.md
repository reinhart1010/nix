---
layout: page
title: common/mitmproxy (español)
description: "Un proxy HTTP interactivo man-in-the-middle."
content_hash: 15ea6f73666ab4f97b8f44bf4bae93473c2f84f9
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/mitmproxy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mitmproxy

Un proxy HTTP interactivo man-in-the-middle.
Vea también: `mitmweb` y `mitmdump`.
Más información: <https://docs.mitmproxy.org/stable/>.

- Inicia `mitmproxy` con la configuración por defecto (escuchará en el puerto `8080`):

`mitmproxy`

- Inicia `mitmproxy` con una dirección y puerto personalizados:

`mitmproxy --listen-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--listen-port</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Inicia `mitmproxy` utilizando un script para procesar el tráfico:

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-s|--scripts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/script.py</span>

- Exporta los registros con las claves maestras SSL/TLS a programas externos (wireshark, etc.):

`SSLKEYLOGFILE="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo</span>`" mitmproxy`

- Especifica el modo de funcionamiento del servidor proxy (`regular` es el predeterminado):

`mitmproxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--mode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular|transparent|socks5|...</span>

- Configura el diseño de la consola:

`mitmproxy --console-layout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">horizontal|single|vertical</span>
