---
layout: page
title: common/npm (español)
description: "Gestor de paquetes JavaScript y Node.js."
content_hash: f98a1da1255e9d0ba534727b90ea7f954ebbfd2e
last_modified_at: 2024-09-27
related_topics:
  - title: Deutsch version
    url: /de/common/npm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/npm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npm

Gestor de paquetes JavaScript y Node.js.
Gestiona proyectos Node.js y sus dependencias de módulos.
Más información: <https://www.npmjs.com>.

- Crea un archivo `package.json` con los valores por defecto (omite --yes para hacerlo de forma interactiva):

`npm init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-y|--yes</span>

- Descarga todos los paquetes listados como dependencias en `package.json`:

`npm install`

- Descarga una versión específica de un paquete y lo añade a la lista de dependencias en `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Descarga la última versión de un paquete y lo añade a la lista de dependencias de desarrollo en `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-D|--save-dev</span>

- Descarga la última versión de un paquete y lo instala globalmente:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

- Desinstala un paquete y lo elimina de la lista de dependencias en `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

- Lista de dependencias instaladas localmente:

`npm list`

- Lista los paquetes instalados globalmente:

`npm list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-g|--global</span>` --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
