---
layout: page
title: common/git-stash (español)
description: "Almacena los cambios locales de Git en un área temporal."
content_hash: 5664a1e8151f0a78801df61bc370f8dfc1b649d3
last_modified_at: 2024-01-10
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
  - title: Türkçe version
    url: /tr/common/git-stash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git stash

Almacena los cambios locales de Git en un área temporal.
Más información: <https://git-scm.com/docs/git-stash>.

- Almacena los cambios actuales, excepto los archivos nuevos (sin seguimiento):

`git stash push -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje_opcional_stash</span>

- Almacena los cambios actuales, incluyendo los archivos nuevos (sin seguimiento):

`git stash -u`

- Selecciona interactivamente partes de los archivos modificados para almacenarlos:

`git stash -p`

- Lista todos los stashes (muestra el nombre del stash, la rama relacionada y el mensaje):

`git stash list`

- Muestra los cambios como un parche entre el stash (por defecto es `stash@{0}`) y la confirmación de cuando se creó la entrada stash por primera vez:

`git stash show -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stash@{0}</span>

- Aplica un stash (por defecto es el último, llamado `stash@{0}`):

`git stash apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_opcional_del_stash_o_confirmación</span>

- Suelta o aplica un stash (por defecto es `stash@{0}`) y lo elimina de la lista de stash si su aplicación no causa conflictos:

`git stash pop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_opcional_stash</span>

- Elimina todos los stashes:

`git stash clear`
