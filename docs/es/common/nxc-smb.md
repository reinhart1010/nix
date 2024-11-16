---
layout: page
title: common/nxc-smb (español)
description: "Prueba y explota servidores SMB."
content_hash: 004b10214def5ea9f85313ae9c2aca5b5a290bd1
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/nxc-smb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nxc-smb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nxc smb

Prueba y explota servidores SMB.
Más información: <https://www.netexec.wiki/smb-protocol>.

- Busca credenciales de dominio válidas probando cada combinación en las listas especificadas de nombres de [u]suario y contraseñas:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nombres_de_usuario.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/contraseñas.txt</span>

- Busca credenciales válidas para cuentas locales en lugar de cuentas de dominio:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nombres_de_usuario.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/contraseñas.txt</span>` --local-auth`

- Enumera los recursos compartidos SMB y los derechos de acceso de los usuarios especificados en los hosts de destino:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.0/24</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` --shares`

- Enumera las interfaces de red en los hosts de destino, realizando la autenticación mediante pass-the-hash:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.30-45</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">NTLM_hash</span>` --interfaces`

- Analiza los hosts de destino en busca de vulnerabilidades frecuentes:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/lista_objetivo.txt</span>` -u '' -p '' -M zerologon -M petitpotam`

- Intenta ejecutar un comando en los hosts de destino:

`nxc smb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
