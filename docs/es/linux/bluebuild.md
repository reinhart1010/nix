---
layout: page
title: linux/bluebuild (español)
description: "Construye Containerfiles e imágenes personalizadas basadas en tu `recipe.yml`."
content_hash: e7a326c9f5238063405d91bf6af2ffc69beec7a9
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/bluebuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluebuild

Construye Containerfiles e imágenes personalizadas basadas en tu `recipe.yml`.
Más información: <https://github.com/blue-build/cli>.

- Construye una receta:

`bluebuild build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/receta.yml</span>

- Valida una receta:

`bluebuild validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/receta.yml</span>

- Genera un archivo contenedor:

`bluebuild generate --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_contenedor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/receta.yml</span>

- Genera una ISO a partir de una receta:

`bluebuild generate-iso --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_salida</span>` --iso-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_iso.iso</span>` recipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/receta.yml</span>

- Muestra la ayuda:

`bluebuild --help`
