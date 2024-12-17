---
layout: page
title: common/pg_dumpall (español)
description: "Extrae un grupo de bases de datos PostgreSQL en un archivo de script u otro archivo de almacenamiento."
content_hash: f5b25cf0fdf18cbba2bebefd2c160a000ec4050f
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/common/pg_dumpall.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pg_dumpall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pg_dumpall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pg_dumpall

Extrae un grupo de bases de datos PostgreSQL en un archivo de script u otro archivo de almacenamiento.
Más información: <https://www.postgresql.org/docs/current/app-pg-dumpall.html>.

- Vuelca todas las bases de datos:

`pg_dumpall > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Vuelca todas las bases de datos utilizando un nombre de usuario específico:

`pg_dumpall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-U|--username</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Lo mismo que antes, usando un equipo y puerto:

`pg_dumpall -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_resultado.sql</span>

- Recupera solo datos de las bases de datos en un archivo script-SQL:

`pg_dumpall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--data-only</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Vuelca solo el esquema (definiciones de datos) en un archivo script-SQL:

`pg_dumpall -s > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_resultado.sql</span>
