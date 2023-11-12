---
layout: page
title: common/git-rebase (español)
description: "Vuelve a aplicar commits de una rama en lo más alto de otra rama."
content_hash: d1cfac2c542363a4c2be35048d83017eca97a906
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-rebase.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-rebase.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rebase.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rebase.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-rebase.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rebase.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/git-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rebase

Vuelve a aplicar commits de una rama en lo más alto de otra rama.
Se utiliza comúnmente para "mover" una rama entera a otra base, ya que crea copias de los commits en una nueva ubicación.
Más información: <https://git-scm.com/docs/git-rebase>.

- Reorganiza la rama actual en lo más alto de otra rama:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_de_reorganización</span>

- Inicia un rebase interactivo que permite reordenar los commits, omitirlos, combinarlos o modificarlos:

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_base_objetivo_o_hash_del_commit</span>

- Continúa un rebase que fue interrumpido por una fusión fallida después de editar los archivos con conflictos:

`git rebase --continue`

- Continúa un rebase que fue pausado para fusionar conflictos saltando el commit conflictivo:

`git rebase --skip`

- Cancela un rebase en proceso (por ej., si es interrumpido por un conflicto de fusión):

`git rebase --abort`

- Mueve parte de la rama actual a una nueva base proporcionando la base antigua para empezar:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_nueva</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_antigua</span>

- Reaplica los últimos 5 commits en su lugar, evita que puedan ser reordenados, omitidos, combinados o modificados:

`git rebase -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Resuelve automáticamente cualquier conflicto favoreciendo la versión de la rama en la que se está trabajando (en este caso la palabra `theirs` tiene un significado invertido):

`git rebase -X theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_de_reorganización</span>
