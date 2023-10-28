---
layout: page
title: common/npm (español)
description: "Gestor de paquetes JavaScript y Node.js."
content_hash: 1967f63aac2f77abc73d2d063d5b065111760014
last_modified_at: 2023-10-28
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
---
# npm

Gestor de paquetes JavaScript y Node.js.
Gestiona proyectos de Node.js y sus módulos de dependencias.
Más información: <https://www.npmjs.com>.

- Creación interactiva de un archivo `package.json`:

`npm init`

- Descarga todos los paquetes listados como dependencias en `package.json`:

`npm install`

- Descarga una versión específica de un paquete y lo añade a la lista de dependencias en `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión</span>

- Descarga la última versión de un paquete y lo añade a la lista de dependencias de desarrollo en `package.json`:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>` --save-dev`

- Descarga la última versión de un paquete y lo instala globalmente:

`npm install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

- Desinstala un paquete y lo remueve de la lista de dependencias en `package.json`:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_paquete</span>

- Lista de dependencias instaladas localmente:

`npm list`

- Lista de paquetes instalados globalmente de nivel superior:

`npm list --global --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
