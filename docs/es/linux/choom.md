---
layout: page
title: linux/choom (español)
description: "Muestra y cambia el ajuste del OOM-killer."
content_hash: 70bd379b86584c25cd4ef0523c4ecc89dac4bc2e
last_modified_at: 2024-03-21
related_topics:
  - title: English version
    url: /en/linux/choom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choom

Muestra y cambia el ajuste del OOM-killer.
Más información: <https://manned.org/choom>.

- Muestra la puntuación OOM-killer del proceso con un identificador específico:

`choom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Modifica la puntuación OOM-killer de un proceso específico:

`choom -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1000..+1000</span>

- Ejecuta un comando con una puntuación OOM-killer específica:

`choom -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1000..+1000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumento1 argumento2 ...</span>
