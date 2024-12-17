---
layout: page
title: common/pg_isready (español)
description: "Comprueba el estado de conexión de un servidor PostgreSQL."
content_hash: df88a092f617bfef7a0ec9f8e19727d3e168d572
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/common/pg_isready.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pg_isready.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pg_isready.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pg_isready

Comprueba el estado de conexión de un servidor PostgreSQL.
Más información: <https://www.postgresql.org/docs/current/app-pg-isready.html>.

- Verifica la conexión:

`pg_isready`

- Revisa la conexión con un nombre de host específico y el puerto:

`pg_isready --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_equipo</span>` --port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Comprueba la conexión mostrando un mensaje solo cuando la conexión falla:

`pg_isready --quiet`
