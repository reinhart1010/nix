---
layout: page
title: common/pgbench (español)
description: "Ejecuta una prueba de referencia (benchmark test) en PostgreSQL."
content_hash: 36db158e6772864e55a9d8dfd27b0ccab200fa08
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/pgbench.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pgbench.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pgbench

Ejecuta una prueba de referencia (benchmark test) en PostgreSQL.
Más información: <https://www.postgresql.org/docs/10/pgbench.html>.

- Inicia una base de datos con un factor de escalamiento de 50 veces el tamaño predeterminado:

`pgbench --initialize --scale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Hace una prueba de referencia a una base de datos con 10 clientes, 2 hilos de trabajo y 10.000 transacciones por cliente:

`pgbench --client=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --jobs=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` --transactions=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>
