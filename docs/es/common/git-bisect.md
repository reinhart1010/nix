---
layout: page
title: common/git-bisect (español)
description: "Utiliza la búsqueda binaria para encontrar la confirmación que introdujo un error."
content_hash: 0820545cb8a0222cd003b903108d63921864cbe7
last_modified_at: 2024-01-13
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
  - title: Indonesia version
    url: /id/common/git-bisect.html
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
tldri18n_status: 2
---
# git bisect

Utiliza la búsqueda binaria para encontrar la confirmación que introdujo un error.
Git salta de un lado a otro del gráfico de confirmaciones hasta alcanzar progresivamente la confirmación defectuosa.
Más información: <https://git-scm.com/docs/git-bisect>.

- Comienza una sesión de bisecado en un rango de confirmaciones delimitado por una confirmación errónea conocida y por una sana conocida (normalmente más antigua):

`git bisect start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación_errónea</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">confirmación_buena</span>

- Para cada confirmación que `git bisect` seleccione, marcala como "mala" (`bad`) o "buena" (`good`) después de probarla para el problema:

`git bisect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">good|bad</span>

- Termina la sesión de bisecado y vuelve a la rama anterior después de que `git-bisect` determine con precisión la confirmación defectuosa:

`git bisect reset`

- Omite una confirmación durante una sesión de bisecado (p. ej. una que falla las pruebas debido a un problema diferente):

`git bisect skip`

- Muestra un registro de lo que se ha hecho hasta el momento:

`git bisect log`
