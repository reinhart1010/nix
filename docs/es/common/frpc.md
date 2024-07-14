---
layout: page
title: common/frpc (español)
description: "Conéctate a un servidor `frps` para iniciar conexiones proxy en el host actual."
content_hash: 0cb666c5831b04736ed98674a5252bee21400e39
last_modified_at: 2024-07-14
related_topics:
  - title: English version
    url: /en/common/frpc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/frpc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# frpc

Conéctate a un servidor `frps` para iniciar conexiones proxy en el host actual.
Parte de `frp`.
Más información: <https://github.com/fatedier/frp>.

- Inicia el servicio, utilizando el archivo de configuración por defecto (se supone que es `frps.ini` en el directorio actual):

`frpc`

- Inicia el servicio, utilizando el nuevo archivo de configuración TOML (`frps.toml` en lugar de `frps.ini`) en el directorio actual:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- Inicia el servicio, utilizando un archivo de configuración específico:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Comprueba si el archivo de configuración es válido:

`frpc verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Imprime script de configuración de autocompletado para Bash, fish, PowerShell o Zsh:

`frpc completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- Muestra versión:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
