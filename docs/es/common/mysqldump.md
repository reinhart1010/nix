---
layout: page
title: common/mysqldump (español)
description: "Crea una copia de seguridad (backup) de bases de datos MySQL."
content_hash: 2d9bdf46275399988a38363ffb71ad4111a9ffbc
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/mysqldump.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mysqldump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysqldump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mysqldump

Crea una copia de seguridad (backup) de bases de datos MySQL.
Vea también `mysql` para restaurar bases de datos.
Más información: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Crea un backup (se le pedirá la contraseña al usuario):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` --result-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Crea un backup de una tabla específica redireccionando la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_tabla</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Crea un backup de todas las bases de datos y redirige la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password --all-databases > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>

- Crea un backup de todas las bases de datos de un host remoto redirigiendo la salida a un archivo (se le pedirá la contraseña al usuario):

`mysqldump --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_o_nombre_de_host</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password --all-databases > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.sql</span>
