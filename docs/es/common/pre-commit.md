---
layout: page
title: common/pre-commit (español)
description: "Crea puntos de enganche Git que se ejecutan antes de la confirmación de cambios."
content_hash: efaa120e1a043d8c48b9f6363cf9b798dcffcbbb
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pre-commit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pre-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pre-commit

Crea puntos de enganche Git que se ejecutan antes de la confirmación de cambios.
Más información: <https://pre-commit.com>.

- Instala pre-commit en tus puntos de enganche Git:

`pre-commit install`

- Ejecuta los puntos de enganche de pre-commit en todos los archivos organizados:

`pre-commit run`

- Ejecuta los puntos de enganche de pre-commit en todos los archivos, organizados o no:

`pre-commit run --all-files`

- Limpia la caché de pre-commit:

`pre-commit clean`

- Actualiza el archivo de configuración de pre-commit a las últimas versiones de los repositorios:

`pre-commit autoupdate`
