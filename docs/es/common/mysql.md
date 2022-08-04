---
layout: page
title: common/mysql (español)
description: "Herramienta de línea de comandos para gestionar bases de datos MySQL."
content_hash: cdb6e6e80cc113275ce3bab2b92471126ffb11d3
related_topics:
  - title: English version
    url: /en/common/mysql.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/mysql.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/mysql.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mysql.html
    icon: bi bi-globe
---
# mysql

Herramienta de línea de comandos para gestionar bases de datos MySQL.
Más información: <https://www.mysql.com/>.

- Conecta a una base de datos:

`mysql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Conecta a una base de datos con el usuario `usuario` y se le pedirá la contraseña:

`mysql -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Conecta a una base de datos en otra máquina:

`mysql -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maquina_remota</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Conecta a una base de datos a través de un socket unix:

`mysql --socket `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/socket.sock</span>

- Ejecuta comandos SQL contenidos en un script:

`mysql -e "source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.sql</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>

- Restaura una base de datos a partir de una copia de seguridad creada con `mysqldump` (y se le pedirá la contraseña al usuario):

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_base_de_datos</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/backup.sql</span>

- Restaura todas las bases de datos en una copia de seguridad (y se le pedirá la contraseña al usuario):

`mysql --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/backup.sql</span>
