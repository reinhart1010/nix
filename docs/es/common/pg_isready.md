---
layout: page
title: common/pg_isready (español)
description: "Comprueba el estado de conexión de un servidor PostgreSQL."
content_hash: df88a092f617bfef7a0ec9f8e19727d3e168d572
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/pg_isready.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pg_isready.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pg_isready

Comprueba el estado de conexión de un servidor PostgreSQL.
Más información: <https://www.postgresql.org/docs/current/app-pg-isready.html>.

- Verifica la conexión:

`pg_isready`

- Revisa la conexión con un nombre de host específico y el puerto:

`pg_isready --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_equipo</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Comprueba la conexión mostrando un mensaje solo cuando la conexión falla:

`pg_isready --quiet`
