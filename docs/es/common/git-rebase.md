---
layout: page
title: common/git-rebase (español)
description: "Vuelve a aplicar confirmaciones de una rama en lo más alto de otra rama."
content_hash: d1ffea3204b1f94edb516794c5946ced4946c30b
last_modified_at: 2024-09-27
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
  - title: 한국어 version
    url: /ko/common/git-rebase.html
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

Vuelve a aplicar confirmaciones de una rama en lo más alto de otra rama.
Se utiliza comúnmente para "mover" una rama entera a otra base, ya que crea copias de las confirmaciones en una nueva ubicación.
Más información: <https://git-scm.com/docs/git-rebase>.

- Reorganiza la rama actual en lo más alto de otra rama:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nueva_base_rama</span>

- Inicia un rebase interactivo que permite reordenar, omitir, combinar o modificar confirmaciones:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rama_base_objetivo_o_hash_de_la_confirmación</span>

- Continúa un rebase que fue interrumpido por una fusión fallida después de editar los archivos con conflictos:

`git rebase --continue`

- Continúa un rebase que fue pausado para fusionar conflictos saltando la confirmación conflictiva:

`git rebase --skip`

- Cancela un rebase en proceso (por ej., si es interrumpido por un conflicto de fusión):

`git rebase --abort`

- Mueve parte de la rama actual a una nueva base proporcionando la base antigua para empezar:

`git rebase --onto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_nueva</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">base_antigua</span>

- Reaplica las últimas cinco confirmaciones en su lugar, evita que puedan ser reordenadas, omitidas, combinadas o modificadas:

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--interactive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD~5</span>

- Resuelve automáticamente cualquier conflicto favoreciendo la versión de la rama en la que se está trabajando (en este caso la palabra `theirs` tiene un significado invertido):

`git rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-X|--strategy-option</span>` theirs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_rama</span>
