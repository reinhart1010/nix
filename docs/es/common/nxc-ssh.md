---
layout: page
title: common/nxc-ssh (español)
description: "Prueba y explota servidores SSH."
content_hash: b787409157efd79fd3feec0023fac4fef87b4252
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/nxc-ssh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nxc-ssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nxc ssh

Prueba y explota servidores SSH.
Vea también: `hydra`.
Más información: <https://www.netexec.wiki/ssh-protocol>.

- Pulveriza la contraseña especificada contra una lista de nombres de usuario en el objetivo especificado:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nombres_de_usuario.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>

- Busca credenciales válidas probando todas las combinaciones de nombres de usuario y contraseñas de las listas especificadas:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nombres_de_usuario.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/contraseñas.txt</span>

- Utiliza la clave privada especificada para la autenticación, utilizando la contraseña suministrada como frase de contraseña de la clave:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.186.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/nombres_de_usuario.txt</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` --key-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/id_rsa</span>

- Prueba una combinación de nombres de usuario y contraseñas en una serie de objetivos:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.0/24</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>

- Comprueba los privilegios `sudo` en un inicio de sesión correcto:

`nxc ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/contraseñas.txt</span>` --sudo-check`
