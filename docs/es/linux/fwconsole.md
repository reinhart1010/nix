---
layout: page
title: linux/fwconsole (español)
description: "Gestiona y configura un sistema FreePBX (servidor PBX)."
content_hash: 745aad77b453ac9cdc772fb00a755243bdcab1b2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/fwconsole.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fwconsole

Gestiona y configura un sistema FreePBX (servidor PBX).
Más información: <https://sangomakb.atlassian.net/wiki/spaces/PG/pages/41779247/fwconsole+commands+13>.

- Recarga las configuraciones de FreePBX:

`fwconsole reload`

- Inicia Asterisk y otros comandos necesarios para FreePBX:

`fwconsole start`

- Detiene Asterisk y otros comandos necesarios para FreePBX:

`fwconsole stop`

- Visualiza y actualiza la configuración:

`fwconsole setting `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabra_clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nuevo_valor</span>

- Lista las copias de seguridad disponibles:

`fwconsole backup --list`

- Lista de comandos FreePBX disponibles:

`fwconsole list`

- Cambia la propiedad de todos los archivos y directorios que FreePBX necesita que sean propiedad del usuario apache:

`fwconsole chown`
