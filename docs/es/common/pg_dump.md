---
layout: page
title: common/pg_dump (español)
description: "Extrae una base de datos PostgreSQL en un archivo de script u otro archivo de almacenamiento."
content_hash: 641462d4921bf26af7e5c9d6bbe1ad8289a2b0a9
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/pg_dump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pg_dump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pg_dump

Extrae una base de datos PostgreSQL en un archivo de script u otro archivo de almacenamiento.
Más información: <https://www.postgresql.org/docs/current/app-pgdump.html>.

- Vuelca la base de datos en un archivo script-SQL:

`pg_dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_resultado.sql</span>

- Igual que antes usando además un nombre de usuario:

`pg_dump -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_resultado.sql</span>

- Lo mismo que antes usando además equipo y puerto:

`pg_dump -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">equipo</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_resultado.sql</span>

- Vuelca una base de datos en un archivo de formato personalizado:

`pg_dump -Fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_resultado.dump</span>

- Recupera solo datos de bases de datos en un archivo script-SQL:

`pg_dump -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado.sql</span>

- Vuelca solo el esquema (definiciones de datos) en un archivo script-SQL:

`pg_dump -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado.sql</span>
