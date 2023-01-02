---
layout: page
title: common/amass-track (español)
description: "Seguimiento de las diferencias entre enumeraciones del mismo dominio."
content_hash: c15ce8254cdfa965d0e19ce96384fa60b90c96e9
last_modified_at: 2023-01-02
related_topics:
  - title: English version
    url: /en/common/amass-track.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-track.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># amass track

Seguimiento de las diferencias entre enumeraciones del mismo dominio.
Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- Muestra la diferencia entre las últimas enumeraciones de un dominio específico:

`amass track -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_de_base_de_datos</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>` -last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..infinity</span>

- Muestra la diferencia entre un momento determinado y la última enumeración:

`amass track -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_de_base_de_datos</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_dominio</span>` -since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01/02 15:04:05 2006 MST</span>
