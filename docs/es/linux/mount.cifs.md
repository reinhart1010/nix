---
layout: page
title: linux/mount.cifs (español)
description: "Monta SMB (Server Message Block) o CIFS (Common Internet File System)."
content_hash: 6ea33d86231e22f960286bb5b0823787f47d4742
last_modified_at: 2024-11-18
related_topics:
  - title: English version
    url: /en/linux/mount.cifs.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mount.cifs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/mount.cifs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mount.cifs

Monta SMB (Server Message Block) o CIFS (Common Internet File System).
Nota: también puede hacer lo mismo pasando la opción `-t cifs` a `mount`.
Más información: <https://manned.org/mount.cifs>.

- Conecta el nombre de usuario especificado o `$USER` por defecto (se le pedirá una contraseña):

`mount.cifs -o user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">punto_de_montaje</span>

- Conecta como usuario invitado (sin contraseña):

`mount.cifs -o guest //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">punto_de_montaje</span>

- Establece información de propiedad para el directorio montado:

`mount.cifs -o uid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_usuario|usuario</span>`,gid=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_del_grupo|nombre_del_grupo</span>` //`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_share</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">punto_de_montaje</span>
