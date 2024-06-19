---
layout: page
title: common/neo4j-admin (español)
description: "Gestiona y administra un Neo4j DBMS (Sistema de Gestión de Bases de Datos)."
content_hash: b386efdd07c94f41120960a5ea8a28636445b7b2
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/neo4j-admin.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/neo4j-admin.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># neo4j-admin

Gestiona y administra un Neo4j DBMS (Sistema de Gestión de Bases de Datos).
Más información: <https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/>.

- Inicia el DBMS:

`neo4j-admin server start`

- Detén el DBMS:

`neo4j-admin server stop`

- Establece la contraseña inicial del usuario predeterminada `neo4j` (requisito para el primer arranque del DBMS):

`neo4j-admin dbms set-initial-password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Crea un archivo con una base de datos sin conexión llamado `nombre_base_de_datos.dump`:

`neo4j-admin database dump --to-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_base_de_datos</span>

- Carga una base de datos desde un archivo llamado `nombre_base_de_datos.dump`:

`neo4j-admin database load --from-path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_base_de_datos</span>` --overwrite-destination=true`

- Carga una base de datos desde un archivo especificado a través de `stdin`:

`neo4j-admin database load --from-stdin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_base_de_datos</span>` --overwrite-destination=true < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nombre_archivo.dump</span>

- Muestra ayuda:

`neo4j-admin --help`
