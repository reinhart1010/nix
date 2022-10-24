---
layout: page
title: common/git-imerge (español)
description: "Ejecuta una fusión o rebase entre dos ramas Git incrementalmente."
content_hash: fd0e91721bfb068ce4f54dd3d45ff60a4c1c1257
related_topics:
  - title: English version
    url: /en/common/git-imerge.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-imerge.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-imerge.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-imerge.html
    icon: bi bi-globe
---
# git-imerge

Ejecuta una fusión o rebase entre dos ramas Git incrementalmente.
Los conflictos entre las ramas se rastrean a pares de commits individuales para simplificar la resolución de conflictos.
Más información: <https://github.com/mhagger/git-imerge>.

- Inicia un rebase de tipo imerge (primero comprueba la rama a ser rebasada):

`git imerge rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_a_rebasar</span>

- Inicia una fusión de tipo imerge (primero comprueba la rama en la que fusionar):

`git imerge merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_a_fusionar</span>

- Muestra una diagrama ASCII para la fusión o rebase en proceso:

`git imerge diagram`

- Continua la operación imerge después de resolver los conflictos (primero añade con `git add` los archivos conflictivos):

`git imerge continue --no-edit`

- Concluye una operación imerge después de que todos los conflictos se hayan resuelto:

`git imerge finish`

- Aborta una operación imerge y vuelve a la rama anterior:

`git-imerge remove && git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_anterior</span>
