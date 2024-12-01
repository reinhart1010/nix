---
layout: page
title: common/wikiman (español)
description: "Motor de búsqueda sin conexión para documentación."
content_hash: a42fbb0cf9b8e787491ff471abc5c425a6a682e1
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/common/wikiman.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wikiman

Motor de búsqueda sin conexión para documentación.
Soporta páginas de manuales, Arch Wiki, Gentoo Wiki, documentación de FreeBSD y tldr-pages.
Más información: <https://github.com/filiparag/wikiman>.

- Busca un tema específico en todas las fuentes instaladas:

`wikiman `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Busca un tema en una fuente específica:

`wikiman -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fuente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Busca un tema en dos o más fuentes específicas:

`wikiman -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fuente1,fuente2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">término_de_búsqueda</span>

- Lista de fuentes existentes:

`wikiman -S`

- Muestra ayuda:

`wikiman -h`
