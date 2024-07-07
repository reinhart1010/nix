---
layout: page
title: common/cypher-shell (español)
description: "Abre una sesión interactiva y ejecuta consultas Cypher contra una instancia Neo4j."
content_hash: f6889dde40002f721db2b3beacf572fce2334683
last_modified_at: 2024-07-07
related_topics:
  - title: English version
    url: /en/common/cypher-shell.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cypher-shell.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cypher-shell

Abre una sesión interactiva y ejecuta consultas Cypher contra una instancia Neo4j.
Vea también: `neo4j-admin`, `mysql`.
Más información: <https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/>.

- Conéctate a una instancia local en el puerto por defecto (`neo4j://localhost:7687`):

`cypher-shell`

- Conéctate a una instancia remota:

`cypher-shell --address neo4j://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>

- Conéctate y proporciona credenciales de seguridad:

`cypher-shell --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>

- Conéctate a una base de datos específica:

`cypher-shell --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Ejecuta sentencias Cypher en un archivo y lo cierra:

`cypher-shell --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.cypher</span>

- Activa el registro en un archivo:

`cypher-shell --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.log</span>

- Muestra ayuda:

`cypher-shell --help`
