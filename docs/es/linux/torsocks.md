---
layout: page
title: linux/torsocks (español)
description: "Enruta el tráfico de cualquier aplicación a través de la red Tor."
content_hash: 7e1723084ce8cfdc59f8b4032d9f9c5dc749622b
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/linux/torsocks.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># torsocks

Enruta el tráfico de cualquier aplicación a través de la red Tor.
Nota: `torsocks` asumirá que debe conectarse al proxy SOCKS que corre en 127.0.0.1:9050 que es el servicio (daemon) predeterminado de Tor.
Más información: <https://gitlab.torproject.org/tpo/core/torsocks/>.

- Ejecuta un comando usando Tor:

`torsocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Activa o desactiva Tor en este intérprete de comandos:

`. torsocks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Lanza una nueva interfaz de comando habilitada con Tor:

`torsocks --shell`

- Revisa si la interfaz de comando actual está habilitada con Tor (`LD_PRELOAD` este valor estará vacío si no está habilitada):

`torsocks show`

- Aísla el tráfico a través de un circuito Tor diferente, mejorando el anonimato:

`torsocks --isolate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">curl https://check.torproject.org/api/ip</span>

- Se conecta a un proxy Tor que se ejecuta en una dirección y un puerto específico:

`torsocks --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
