---
layout: page
title: common/git-submodule (español)
description: "Inspecciona, actualiza y gestiona los submódulos."
content_hash: 34b03160dbebe37234f1b98f280ece311453d02a
related_topics:
  - title: English version
    url: /en/common/git-submodule.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-submodule.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-submodule.html
    icon: bi bi-globe
---
# git submodule

Inspecciona, actualiza y gestiona los submódulos.
Más información: <https://git-scm.com/docs/git-submodule>.

- Instala los submódulos específicos de un repositorio:

`git submodule update --init --recursive`

- Añade un repositorio como un submódulo:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_repositorio</span>

- Añade un repositorio Git como submulo en un directorio específico:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_repositorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Actualiza cada submódulo a su último commit:

`git submodule foreach git pull`
