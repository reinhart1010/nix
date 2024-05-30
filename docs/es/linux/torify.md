---
layout: page
title: linux/torify (español)
description: "Enruta el tráfico de red a través de la red Tor."
content_hash: 1935a6dad86dcae39806c82fa796eb7e97ccde24
last_modified_at: 2024-05-30
related_topics:
  - title: English version
    url: /en/linux/torify.html
    icon: bi bi-globe
tldri18n_status: 2
---
# torify

Enruta el tráfico de red a través de la red Tor.
Nota: Este comando está desfasado, y ahora es un empaquetador compatible con versiones anteriores de `torsocks`.
Más información: <https://manned.org/man/torify>.

- Enruta el tráfico a través de Tor:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Activa o desactiva Tor en el intérprete de comandos:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Crea un intérprete de órdenes con Tor activado:

`torify --shell`

- Checa si hay un intérprete de órdenes con Tor activado:

`torify show`

- Especifica el archivo de configuración de Tor:

`torify -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_configuración</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Usa un proxy Tor SOCKS específico:

`torify -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proxy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Redirige la salida a un archivo:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_de_salida</span>
