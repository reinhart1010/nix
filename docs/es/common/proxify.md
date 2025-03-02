---
layout: page
title: common/proxify (español)
description: "Un proxy versátil y portátil para capturar, manipular y reproducir tráfico HTTP/HTTPS sobre la marcha."
content_hash: db38444c0648ae296a4f7fb2e356b01aea971956
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/proxify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# proxify

Un proxy versátil y portátil para capturar, manipular y reproducir tráfico HTTP/HTTPS sobre la marcha.
Vea también: `mitmproxy`.
Más información: <https://github.com/projectdiscovery/proxify>.

- Inicia un proxy HTTP (en la interfaz de red loopback `127.0.0.1` y puerto `8888`):

`proxify`

- Inicia un proxy HTTP en una interfaz de red y puerto personalizados (puede requerir `sudo` para un número de puerto inferior a `1024`):

`proxify -http-addr "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dirección_ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_puerto</span>`"`

- Especifica el formato y el archivo de salida:

`proxify -output-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jsonl|yaml</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra la ayuda:

`proxify -h`
