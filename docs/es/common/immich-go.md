---
layout: page
title: common/immich-go (español)
description: "Immich-Go es una herramienta abierta diseñada para subir grandes colecciones de fotos a tu servidor Immich autoalojado."
content_hash: 2a6a951a3fedb4e57afab3748a74284322fdbd16
last_modified_at: 2024-05-07
related_topics:
  - title: English version
    url: /en/common/immich-go.html
    icon: bi bi-globe
tldri18n_status: 2
---
# immich-go

Immich-Go es una herramienta abierta diseñada para subir grandes colecciones de fotos a tu servidor Immich autoalojado.
Véase también: `immich-cli`.
Más información: <https://github.com/simulot/immich-go>.

- Sube un archivo takeout de Google al servidor Immich:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_servidor</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_de_servidor</span>` upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_takeout.zip</span>

- Importa fotos capturadas en junio del 2019, mientras se generan los álbumes automáticamente:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_servidor</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_del_servidor</span>` upload -create-albums -google-photos -date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2019-06</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_takeout.zip</span>

- Sube un archivo usando servidor y clave de un archivo de configuración:

`immich-go -use-configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.immich-go/immich-go.json</span>` upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_takeout.zip</span>

- Examina el contenido del servidor Immich, elimina las imágenes de menor calidad y preserva álbumes:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_servidor</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_del_servidor</span>` duplicate -yes`

- Elimina todos los álbumes creados con el patrón "YYYY-MM-DD":

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_servidor</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_del_servidor</span>` tool album delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\d{4}-\d{2}-\d{2}</span>
