---
layout: page
title: common/usql (español)
description: "Interfaz de línea de comandos universal para bases de datos SQL."
content_hash: 7b9e9a76d43c77846a9d8775191eba355dc6d0eb
last_modified_at: 2024-03-05
related_topics:
  - title: English version
    url: /en/common/usql.html
    icon: bi bi-globe
tldri18n_status: 2
---
# usql

Interfaz de línea de comandos universal para bases de datos SQL.
Más información: <https://github.com/xo/usql>.

- Conecta a una base de datos específica:

`usql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sqlserver|mysql|postgres|sqlite3|...</span>`://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Ejecuta comandos desde un archivo:

`usql --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/query.sql</span>

- Ejecuta un comando SQL específico:

`usql --command="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_sql</span>`"`

- Lista las bases de datos disponibles en el servidor:

`usql --list-databases`

- Ejecuta un comando SQL en el indicador `usql`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Muestra el esquema de la base de datos:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\d</span>

- Exporta los resultados de la consulta a un archivo específico:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/resultados.txt</span>

- Importa datos de un archivo CSV a una tabla específica:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prompt</span>`=> \copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/datos.csv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_tabla</span>
