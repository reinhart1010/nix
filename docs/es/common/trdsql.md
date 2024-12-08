---
layout: page
title: common/trdsql (español)
description: "Ejecuta SQL en archivos CSV, LTSV, JSON, YAML y TBLN."
content_hash: c5c68d434afadc742df77a29e29c58ba1dc63031
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/trdsql.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/trdsql.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># trdsql

Ejecuta SQL en archivos CSV, LTSV, JSON, YAML y TBLN.
Más información: <https://noborus.github.io/trdsql/>.

- Convierte datos de objetos de varios archivos JSON a un archivo CSV con encabezado (`-oh`) y comillas dobles:

`trdsql -ocsv -oh "SELECT * FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo/*.json</span>`" | sed 's/\([^,]*\)/«&»/g' > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.csv</span>

- Interpreta una lista JSON como tabla y pone objetos dentro como columnas ( ruta/al/archivo.json: `{"lista":[{"edad":"26", "nombre":"Tanaka"}]}`):

`trdsql "SELECT * FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.json</span>`::.list`

- Manipula una consulta SQL compleja con datos de varios archivos CSV cuya primera línea es la cabecera (`-ih`):

`trdsql -icsv -ih "SELECT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna1,columna2</span>` FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo*.csv</span>` WHERE column2 != '' ORDER BY columna1 GROUP BY columna1"`

- Combina el contenido de 2 archivos CSV en un archivo CSV:

`trdsql "SELECT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna1,columna2</span>` FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.csv</span>` UNION SELECT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna1,columna2</span>` FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.csv</span>`"`

- Se conecta a la base de datos PostgreSQL:

`trdsql -driver postgres -dsn "host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_host</span>` port=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5433</span>` dbname=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_base_de_datos</span>`" "SELECT 1"`

- Crea una tabla de datos en una base de datos MySQL a partir de un archivo CSV:

`trdsql -driver mysql -dsn "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_host</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_de_datos</span>`" -ih "CREATE TABLE `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tabla</span>` (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna1</span>` int, `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna2</span>` varchar(20)) AS SELECT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna3</span>` AS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">columna2</span>` FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_cabecera.csv</span>`"`

- Muestra datos de archivos de registro comprimidos:

`trdsql -iltsv "SELECT * FROM `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/acceso.log.gz</span>`"`
