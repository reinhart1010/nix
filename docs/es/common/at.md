---
layout: page
title: common/at (español)
description: "Ejecuta los comandos una vez en otro momento."
content_hash: 2861742c30031e06bdfade48c54f076e94e6a4e0
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Ejecuta los comandos una vez en otro momento.
Los resultados se enviarán al correo del usuario.
Más información: <https://manned.org/at>.

- Inicia el servicio (daemon)`atd`:

`systemctl start atd`

- Crea comandos interactivamente y los ejecuta en 5 minutos (pulsa `<Ctrl> + D` cuando termines):

`at now + 5 minutes`

- Crea comandos de forma interactiva y los ejecuta a una hora determinada:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Ejecuta un comando de `stdin` a las 10:00 AM de hoy:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`" | at 1000`

- Ejecuta comandos desde un archivo determinado el próximo martes:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` 9:30 PM Tue`
