---
layout: page
title: common/git-tag (español)
description: "Crea, muestra, borra o verifica etiquetas."
content_hash: 22d191495c3d29ae933aa20fa6670e2977f73cff
related_topics:
  - title: Deutsch version
    url: /de/common/git-tag.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-tag.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-tag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
---
# git tag

Crea, muestra, borra o verifica etiquetas.
Una etiqueta es una referencia estática a un commit específico.
Más información: <https://git-scm.com/docs/git-tag>.

- Muestra todas las etiquetas:

`git tag`

- Crea una etiqueta con el nombre especificado a partir del commit actual:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>

- Crea una etiqueta con el nombre especificado a partir del commit señalado:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Crea una etiqueta anotada con el mensaje especificado:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje_de_la_etiqueta</span>

- Elimina la etiqueta con el nombre especificado:

`git tag -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>

- Obtiene las etiquetas actualizadas de upstreams:

`git fetch --tags`

- Muestra todas las etiquetas cuyos ancestros incluyan un commit específico:

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
