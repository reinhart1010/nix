---
layout: page
title: common/medusa (español)
description: "Un forzador bruto de inicio de sesión modular y paralelo para una variedad de protocolos."
content_hash: 7e29f401883ac3242d54baa3bb8bd603452567b0
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/medusa.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/medusa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# medusa

Un forzador bruto de inicio de sesión modular y paralelo para una variedad de protocolos.
Más información: <https://jmk-foofus.github.io/medusa/medusa.html>.

- Lista todos los módulos instalados:

`medusa -d`

- Muestra ejemplo de uso de un módulo específico (usa `medusa -d` para listar todos los módulos instalados):

`medusa -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh|http|web-form|postgres|ftp|mysql|...</span>` -q`

- Ejecuta fuerza bruta contra un servidor FTP utilizando un fichero que contiene nombres de usuario y un fichero que contiene contraseñas:

`medusa -M ftp -h host -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_usuario</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_contraseña</span>

- Ejecuta un intento de inicio de sesión contra un servidor HTTP utilizando el nombre de usuario, la contraseña y el agente de usuario especificados:

`medusa -M HTTP -h host -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` -m USER-AGENT:"`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">agente</span>`"`

- Ejecuta una fuerza bruta contra un servidor MySQL utilizando un fichero que contenga nombres de usuario y un hash:

`medusa -M mysql -h host -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_usuario</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hash</span>` -m PASS:HASH`

- Ejecuta una fuerza bruta contra una lista de servidores SMB utilizando un nombre de usuario y un archivo pwdump:

`medusa -M smbnt -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_hosts</span>` -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_pwdump</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -m PASS:HASH`
