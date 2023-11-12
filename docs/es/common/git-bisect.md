---
layout: page
title: common/git-bisect (español)
description: "Utiliza la búsqueda binaria para encontrar el commit que introdujo un error."
content_hash: 9fdcc4bb8bfb0fd3d3018512d8ba16f21e055a40
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-bisect.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-bisect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bisect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-bisect.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bisect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bisect.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git bisect

Utiliza la búsqueda binaria para encontrar el commit que introdujo un error.
Git salta de un lado a otro del gráfico de commits para hasta alcanzar progresivamente el commit defectuoso.
Más información: <https://git-scm.com/docs/git-bisect>.

- Comienza un sesión de bisecado en un rango de commits delimitada por un commit erróneo conocido y por uno sano conocido (normalmente más antiguo):

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_erroneo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_bueno</span>

- Para cada commit que `git bisect` selecciona, marcarlo como "malo" o "bueno" después de probarlo para el problema:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bueno|malo</span>

- Después de que `git bisect` determine con precisión el commit defectuoso, termina la sesión de bisecado y vuelve a la rama anterior:

`git bisect reset`

- Salta un commit durante una sesión de bisecado (p. ej., uno que falla las pruebas debido a un problema diferente):

`git bisect skip`
