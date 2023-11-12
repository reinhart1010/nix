---
layout: page
title: common/git-restore (español)
description: "Restaura los archivos del árbol de trabajo. Requiere la version 2.23+ de Git."
content_hash: 876c253ae73b38f3859e0c063bc70aa91f80754e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-restore.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-restore.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-restore.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-restore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git restore

Restaura los archivos del árbol de trabajo. Requiere la version 2.23+ de Git.
Véase también `git checkout` y `git reset`.
Más información: <https://git-scm.com/docs/git-restore>.

- Restaura un archivo sin marcar a la versión del commit actual (HEAD):

`git restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Restaura un archivo sin marcar a la versión de un commit específico:

`git restore --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Descarta los cambios sin commit para los archivos rastreados:

`git restore :/`

- Desmarca un archivo:

`git restore --staged `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Desmarca todos los archivos:

`git restore --staged :/`

- Descarta todos los cambios de los archivos, marcados o no:

`git restore --worktree --staged :/`

- Selecciona interactivamente secciones de archivos para restaurar:

`git restore --patch`
