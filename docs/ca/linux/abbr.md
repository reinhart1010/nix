---
layout: page
title: linux/abbr (català)
description: "Gestiona abreviatures per la shell fish."
content_hash: 703b8d2f11105473c6635f2ccb8c0a064d880f1a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/abbr.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/abbr.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/abbr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/abbr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/abbr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/abbr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/abbr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# abbr

Gestiona abreviatures per la shell fish.
Les paraules definides per l'usuari es reemplacen per expresions llarges en introduïr-les.
Més informació: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Afegeix una nova abreviatura:

`abbr --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_abreviatura</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comandament</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>

- Canvia el nom d'una abreviatura existent:

`abbr --rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">antic_nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nou_nom</span>

- Esborra una abreviatura existent:

`abbr --erase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_abreviatura</span>

- Importa les abreviatures definides en un altre host per SSH:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_host</span>` abbr --show | source`
