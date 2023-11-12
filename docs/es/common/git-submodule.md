---
layout: page
title: common/git-submodule (español)
description: "Inspecciona, actualiza y gestiona los submódulos."
content_hash: ca5856064c768ff41370f85b5c8276770bbc4f18
last_modified_at: 2023-11-12
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
  - title: Türkçe version
    url: /tr/common/git-submodule.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git submodule

Inspecciona, actualiza y gestiona los submódulos.
Más información: <https://git-scm.com/docs/git-submodule>.

- Instala los submódulos específicos de un repositorio:

`git submodule update --init --recursive`

- Añade un repositorio como un submódulo:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_repositorio</span>

- Añade un repositorio Git como submódulo en un directorio específico:

`git submodule add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_del_repositorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Actualiza cada submódulo a su último commit:

`git submodule foreach git pull`
