---
layout: page
title: common/jbang (español)
description: "Crea, edita y ejecuta fácilmente programas en Java autocontenidos de sólo código fuente."
content_hash: f56751e7d03be9927a42edf4372a1749b7a49a3b
last_modified_at: 2024-01-29
related_topics:
  - title: English version
    url: /en/common/jbang.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jbang

Crea, edita y ejecuta fácilmente programas en Java autocontenidos de sólo código fuente.
Ver también: `java`.
Más información: <https://www.jbang.dev/documentation/guide/latest/cli/jbang.html>.

- Inicializa una clase en Java simple:

`jbang init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.java</span>

- Inicializa una clase en Java (útil para scripts):

`jbang init --template=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cli</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.java</span>

- Utiliza `jshell` para explorar y utilizar un script y cualquier dependencia en un editor REPL:

`jbang run --interactive`

- Configura un proyecto temporal para editar un script en un entorno de desarrollo integrado:

`jbang edit --open=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">codium|code|eclipse|idea|netbeans|gitpod</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.java</span>

- Ejecuta un fragmento de código en Java (Java 9 y posteriores):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'Files.list(Paths.get("/etc")).forEach(System.out::println);'</span>` | jbang -`

- Ejecuta aplicación de línea de comandos:

`jbang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arg1 arg2 ...</span>

- Instala un script en un directorio en el valor de la variable de entorno `PATH` del usuario actual:

`jbang app install --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/script.java</span>

- Instala una versión específica del JDK para utilizarla con `jbang`:

`jbang jdk install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>
