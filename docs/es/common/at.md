---
layout: page
title: common/at (español)
description: "Ejecuta comandos una vez en un momento posterior."
content_hash: 7a613c15a63d1fd110240699cab69f81aae1c647
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
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

Ejecuta comandos una vez en un momento posterior.
El servicio atd (o atrun) debe estar ejecutándose para las ejecuciones reales.
Más información: <https://manned.org/at>.

- Ejecuta comandos desde la entrada estándar en 5 minutos (pulsa `Ctrl + D` cuando termines):

`at now + 5 minutes`

- Ejecuta un comando desde la entrada estándar a las 10:00 AM de hoy:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at 1000`

- Ejecuta comandos desde un archivo dado el próximo martes:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>` 9:30 PM Tue`
