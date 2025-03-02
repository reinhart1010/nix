---
layout: page
title: linux/autorecon (español)
description: "Herramienta de reconocimiento de red multihilo que realiza una enumeración automatizada de servicios."
content_hash: 6d099fea5fd57ad92aae5cbc10779b2f19447e6f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/autorecon.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/autorecon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autorecon

Herramienta de reconocimiento de red multihilo que realiza una enumeración automatizada de servicios.
Más información: <https://github.com/Tib3rius/AutoRecon>.

- Realiza reconocimiento sobre el(los) host(s) objetivo(s) (los resultados del escaneo detallado se guardarán en `./results`):

`sudo autorecon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_o_ip1,host_o_ip2,...</span>

- Realiza reconocimiento sobre el(los) objetivo(s) desde un archivo:

`sudo autorecon --target-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Guarda los resultados en un directorio diferente:

`sudo autorecon --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/resultados</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_o_ip1,host_o_ip2,...</span>

- Limita el escaneo a [p]uertos y protocolos específicos (`T` para TCP, `U` para UDP, `B` para ambos):

`sudo autorecon --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">T:21-25,80,443,U:53,B:123</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host_o_ip1,host_o_ip2,...</span>
