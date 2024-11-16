---
layout: page
title: common/cypher-shell (español)
description: "Abre una sesión interactiva y ejecuta consultas Cypher contra una instancia Neo4j."
content_hash: 761c61266d989d9626d6b427fec2d7f62c2cd205
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/cypher-shell.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cypher-shell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cypher-shell

Abre una sesión interactiva y ejecuta consultas Cypher contra una instancia Neo4j.
Vea también: `neo4j-admin`, `mysql`.
Más información: <https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>.

- Conéctate a una instancia local en el puerto por defecto (`neo4j://localhost:7687`):

`cypher-shell`

- Conéctate a una instancia remota:

`cypher-shell --address neo4j://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Conéctate y proporciona credenciales de seguridad:

`cypher-shell --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>

- Conéctate a una base de datos específica:

`cypher-shell --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Ejecuta sentencias Cypher en un archivo y lo cierra:

`cypher-shell --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.cypher</span>

- Activa el registro en un archivo:

`cypher-shell --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.log</span>

- Muestra ayuda:

`cypher-shell --help`
