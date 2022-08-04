---
layout: page
title: common/git-lfs (español)
description: "Trabaja con archivos grandes en repositorios de Git."
content_hash: 48447ac56dcc985197b40a0e38694ba20c1c63a0
related_topics:
  - title: English version
    url: /en/common/git-lfs.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-lfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-lfs.html
    icon: bi bi-globe
---
# git lfs

Trabaja con archivos grandes en repositorios de Git.
Más información: <https://git-lfs.github.com>.

- Inicializa Git LFS:

`git lfs install`

- Rastrea archivos que coinciden con un patrón:

`git lfs track '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.bin</span>`'`

- Cambia la URL a la que apunta Git LFS (útil si el servidor LFS está separado del servidor Git):

`git config -f .lfsconfig lfs.url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_punto_de_acceso_LFS</span>

- Muestra los patrones rastreados:

`git lfs track`

- Muestra los archivos que han sido añadidos con un commit:

`git lfs ls-files`

- Introduce todos los objetos LFS en el servidor remoto (útil si se encuentran errores):

`git lfs push --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_remoto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Trae todos los objetos de Git LFS:

`git lfs fetch`

- Verifica todos los objetos de Git LFS:

`git lfs checkout`
