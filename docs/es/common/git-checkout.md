---
layout: page
title: common/git-checkout (español)
description: "Comprueba una rama o rutas con el arbol de trabajo."
content_hash: 70fbee437c83b0f9deb180227e59d54ce8fd3c6c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-checkout.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-checkout.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-checkout.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-checkout.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-checkout.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-checkout.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-checkout.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-checkout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git checkout

Comprueba una rama o rutas con el arbol de trabajo.
Más información: <https://git-scm.com/docs/git-checkout>.

- Crea una nueva rama y cambiarse a esta:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Crea una nueva rama a partir de una referencia específica (rama, remoto/rama, las etiquetas son ejemplos de referencias válidas) y cambiarse a esta:

`git checkout -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">referencia</span>

- Cambia a una rama local existente:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Cambia a la rama previamente comprobada:

`git checkout -`

- Cambia a una rama remota existente:

`git checkout --track `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_remoto</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>

- Descarta todos los cambios sin marcar en el directorio actual (véase `git reset` para más comandos para deshacer):

`git checkout .`

- Decarta los cambios no marcados de un archivo específico:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_archivo</span>

- Sustituir un archivo en el directorio actual con la versión de este en un commit de una rama específica:

`git checkout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_rama</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_archivo</span>
