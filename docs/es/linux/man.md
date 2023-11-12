---
layout: page
title: linux/man (español)
description: "Da formato y muestra páginas del manual."
content_hash: 4296bcc55a1293bc691cda28715e0a09fb56a500
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/man.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/man.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/man.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/man.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/man.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/man.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/man.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/man.html
    icon: bi bi-globe
tldri18n_status: 2
---
# man

Da formato y muestra páginas del manual.
Más información: <https://manned.org/man>.

- Muestra la página del manual para un comando:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Mostrar la página del manual para un comando de la sección 7:

`man `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Listar todas las secciones disponibles para un comando:

`man --whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Muestra las rutas usadas para la búsqueda de las páginas:

`man --path`

- Muestra la ubicación de la página del manual en lugar de la propia página:

`man --where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Muestra la página del manual usando una ubicación específica:

`man --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">locale</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Busca las páginas del manual que contienen la string indicada:

`man --apropos "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_a_buscar</span>`"`
