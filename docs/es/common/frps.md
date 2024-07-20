---
layout: page
title: common/frps (español)
description: "Configura rápidamente un servicio de proxy inverso."
content_hash: c80039399da3a963d31aa7c63c965ca2705982fa
last_modified_at: 2024-07-20
related_topics:
  - title: English version
    url: /en/common/frps.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/frps.html
    icon: bi bi-globe
tldri18n_status: 2
---
# frps

Configura rápidamente un servicio de proxy inverso.
Parte de `frp`.
Más información: <https://github.com/fatedier/frp>.

- Inicia el servicio, utilizando el archivo de configuración por defecto (se supone que es `frps.ini` en el directorio actual):

`frps`

- Inicia el servicio, utilizando el nuevo archivo de configuración TOML (`frps.toml` en lugar de `frps.ini`) en el directorio actual:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Inicia el servicio, utilizando un archivo de configuración especificado:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Comprueba si el archivo de configuración es válido:

`frps verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime script de configuración de autocompletado para Bash, fish, PowerShell o Zsh:

`frps completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Muestra versión:

`frps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
