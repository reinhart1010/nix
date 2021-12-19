---
layout: page
title: common/git-stash (español)
description: "Guarda cambios locales de Git en un área temporal."
content_hash: 51d792e7c0d6e34c8f47e4a85971b76b74d4328e
related_topics:
  - title: English version
    url: /en/common/git-stash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-stash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-stash.html
    icon: bi bi-globe
---
# git stash

Guarda cambios locales de Git en un área temporal.
Más información: <https://git-scm.com/docs/git-stash>.

- Guarda cambios actuales, excepto los archivos nuevos (sin rastrear):

`git stash [push -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje_opcional_del_guardado</span>`]`

- Guarda cambios actuales, incluyendo los archivos nuevos (sin rastrear):

`git stash -u`

- Selecciona interactivamente las partes de archivos cambiados que deben ser guardadas:

`git stash -p`

- Muestra todos los guardados (muestra el nombre del guardado, la rama relacionada y el mensaje):

`git stash list`

- Aplica un guardado (por defecto aplica el último, llamado stash@{0}):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_opcional_del_guardado_o_commit</span>

- Aplica un guardado (por defecto es stash@{0} y lo traslada desde la lista de guardado si no causa conflictos:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_opcional_del_guardado</span>

- Elimina un guardado (por defecto es stash@{0}):

`git stash drop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_opcional_del_guardado</span>

- Elimina todos los guardados:

`git stash clear`
