---
layout: page
title: common/immich-cli (español)
description: "Immich tiene una interfaz de línea de comandos (CLI) que le permite realizar ciertas acciones desde la línea de comandos."
content_hash: cebe5918fecc123be8aa7837d4ec6d9edfb5e436
last_modified_at: 2024-05-07
related_topics:
  - title: English version
    url: /en/common/immich-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# immich-cli

Immich tiene una interfaz de línea de comandos (CLI) que le permite realizar ciertas acciones desde la línea de comandos.
Vea también: `immich-go`.
Más información: <https://immich.app/docs/features/command-line-interface/>.

- Autentica en el servidor de Immich:

`immich login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_servidor/api</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_del_servidor</span>

- Sube unas imágenes:

`immich upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo1.jpg archivo2.jpg</span>

- Sube un directorio y sus subdirectorios:

`immich upload --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Crea un álbum basado en un directorio:

`immich upload --album-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Vacaciones de verano</span>`" --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Omite recursos que coincidan con un patrón global:

`immich upload --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/Raw/** **/*.tif</span>` --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio/</span>

- Incluye archivos ocultos:

`immich upload --include-hidden --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
