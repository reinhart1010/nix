---
layout: page
title: common/msfconsole (español)
description: "Consola para el Metasploit Framework."
content_hash: e5982cec7b5a2359ca2d152ebeb44de1ae412d9d
last_modified_at: 2024-08-05
related_topics:
  - title: English version
    url: /en/common/msfconsole.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msfconsole

Consola para el Metasploit Framework.
Más información: <https://docs.rapid7.com/metasploit/msf-overview>.

- Inicia la consola:

`msfconsole`

- Lanza la consola [q]uietamente sin ningún mensaje:

`msfconsole --quiet`

- No habilita el soporte de bases de datos:

`msfconsole --no-database`

- Ejecuta los comandos de la consola (Nota: utiliza `;` para pasar varios comandos):

`msfconsole --execute-command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">use auxiliary/server/capture/ftp; set SRVHOST 0.0.0.0; set SRVPORT 21; run</span>`"`

- Muestra [v]ersión:

`msfconsole --version`
