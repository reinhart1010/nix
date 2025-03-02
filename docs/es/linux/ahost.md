---
layout: page
title: linux/ahost (español)
description: "Herramienta de búsqueda DNS para mostrar el registro A o AAAA asociado con un nombre de host o dirección IP."
content_hash: 0d2d5c7e5e4b742151934836336791c1a8d8f21d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/ahost.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ahost.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/ahost.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ahost

Herramienta de búsqueda DNS para mostrar el registro A o AAAA asociado con un nombre de host o dirección IP.
Más información: <https://manned.org/ahost>.

- Muestra un registro `A` o `AAAA` asociado con un nombre de host o dirección IP:

`ahost `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Muestra salida adicional de depuración:

`ahost -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Muestra el registro con un tipo especificado:

`ahost -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|aaaa|u</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
