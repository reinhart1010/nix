---
layout: page
title: common/nxc (español)
description: "Herramienta de enumeración y explotación de servicios de red."
content_hash: f944989c73ce23d4b3773b617163d28d603a3cb3
last_modified_at: 2024-10-05
related_topics:
  - title: English version
    url: /en/common/nxc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nxc

Herramienta de enumeración y explotación de servicios de red.
Algunos subcomandos como `smb` tienen su propia documentación de uso.
Más información: <https://www.netexec.wiki/>.

- [L]ista módulos disponibles para el protocolo especificado:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -L`

- Lista las opciones disponibles para el módulo especificado:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>` --options`

- Especifica una opción para un módulo:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NOMBRE_OPCION</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_opción</span>

- Vea las opciones disponibles para el protocolo especificado:

`nxc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql</span>` --help`
