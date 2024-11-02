---
layout: page
title: common/git-tag (español)
description: "Crea, muestra, borra o verifica etiquetas."
content_hash: 2145dfd0effdd030ddb095023cb1ef50d5e20862
last_modified_at: 2024-11-02
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
  - title: 한국어 version
    url: /ko/common/git-tag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-tag.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-tag.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git tag

Crea, muestra, borra o verifica etiquetas.
Una etiqueta (tag) es una referencia estática a una confirmación (commit).
Más información: <https://git-scm.com/docs/git-tag>.

- Muestra todas las etiquetas:

`git tag`

- Crea una etiqueta con el nombre especificado a partir de la confirmación actual:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>

- Crea una etiqueta con el nombre especificado a partir de la confirmación señalada:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>

- Crea una etiqueta anotada con el mensaje especificado:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensaje_de_la_etiqueta</span>

- Elimina la etiqueta con el nombre especificado:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>

- Obtén las etiquetas actualizadas del remoto (remote):

`git fetch --tags`

- Envía una etiqueta al remoto:

`git push origin tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_etiqueta</span>

- Muestra todas las etiquetas cuyos ancestros incluyen una confirmación específica:

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación</span>
