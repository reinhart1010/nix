---
layout: page
title: common/avo (español)
description: "La interfaz oficial de línea de comandos para Avo."
content_hash: dc934b93f04a81adfc09fb11e34f488b046590e0
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/avo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/avo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># avo

La interfaz oficial de línea de comandos para Avo.
Más información: <https://www.avo.app/docs/implementation/cli>.

- Inicializa un espacio de trabajo en el directorio actual:

`avo init`

- Inicia sesión en la plataforma Avo:

`avo login`

- Cambia a una rama Avo existente:

`avo checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_rama</span>

- Extrae las envolturas analíticas de la ruta actual:

`avo pull`

- Muestra el estado de la implementación de Avo:

`avo status`

- Resuelve conflictos Git en archivos Avo:

`avo conflict`

- Abre el espacio de trabajo actual de Avo en el navegador web predeterminado:

`avo edit`

- Muestra la ayuda de un subcomando:

`avo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` --help`
