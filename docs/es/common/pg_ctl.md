---
layout: page
title: common/pg_ctl (español)
description: "Utilidad para controlar un servidor PostgreSQL y un grupo (clúster) de bases de datos."
content_hash: ee1486264a71be12a561b211a5d92baa29b060e7
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/pg_ctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pg_ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pg_ctl

Utilidad para controlar un servidor PostgreSQL y un grupo (clúster) de bases de datos.
Más información: <https://www.postgresql.org/docs/current/app-pg-ctl.html>.

- Inicia un nuevo grupo de base de datos PostgreSQL:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_de_datos</span>` init`

- Inicia un servidor PostgreSQL:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_de_datos</span>` start`

- Detiene un servidor PostgreSQL:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_de_datos</span>` stop`

- Reinicia un servidor PostgreSQL:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_de_datos</span>` restart`

- Recarga la configuración del servidor PostgreSQL:

`pg_ctl -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio_de_datos</span>` reload`
