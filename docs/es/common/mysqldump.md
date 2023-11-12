---
layout: page
title: common/mysqldump (español)
description: "Crea una copia de seguridad de bases de datos MySQL."
content_hash: efbf2721c3b3339bd761b53fc52f600ce220546d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mysqldump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysqldump.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mysqldump

Crea una copia de seguridad de bases de datos MySQL.
Vea también `mysql` para restaurar bases de datos.
Más información: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Crea un backup (se le pedirá la contraseña al usuario):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Crea un backup de todas las bases de datos y redirige la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password --all-databases > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Crea un backup de una única tabla de una base de datos (se le pedirá la contraseña al usuario):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_tabla</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>
