---
layout: page
title: common/autossh (español)
description: "Ejecuta, monitorea y reinicia conexiones SSH."
content_hash: 8ffada3faeaec54307bc118c95cd6d74538ddd3e
last_modified_at: 2023-05-20
related_topics:
  - title: English version
    url: /en/common/autossh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autossh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autossh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/autossh.html
    icon: bi bi-globe
---
# autossh

Ejecuta, monitorea y reinicia conexiones SSH.
Auto-reconecta para mantener los túneles de reenvío de puertos. Acepta todas las señales `ssh`.
Más información: <https://www.harding.motd.ca/autossh>.

- Inicia una sesión SSH, reiniciando cuando un puerto de monitoreo no retorna datos:

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_monitor</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>`"`

- Reenvía un puerto local a uno remoto, reiniciando cuando sea necesario:

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_monitor</span>` -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_local</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Crea un proceso `autossh` en segundo plano antes de ejecutar `ssh` y no abre un shell remoto:

`autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_monitor</span>` -N "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>`"`

- Ejecuta en segundo plano, sin puerto de monitorización, y en su lugar envía paquetes SSH keep-alive cada 10 segundos para detectar fallos:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>`"`

- Ejecuta en segundo plano, sin puerto de monitorización y sin shell remoto, saliendo si falla el reenvío de puerto:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local_port</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_remoto}</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Se ejecuta en segundo plano, registrando la salida de depuración `autossh` y la salida detallada `ssh` en archivos:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/autossh_log_file.log</span>` autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puerto_monitor</span>` -v -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_ssh_log.log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>
