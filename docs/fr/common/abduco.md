---
layout: page
title: common/abduco (français)
description: "Manageur de session dans un terminal."
content_hash: dde657c0716aa99b3b12a60f572c9cf00b63be0f
related_topics:
  - title: English version
    url: /en/common/abduco.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/abduco.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/abduco.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/abduco.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/abduco.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/abduco.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># abduco

Manageur de session dans un terminal.
Plus d'informations : <http://www.brain-dump.org/projects/abduco/>.

- Affiche les sessions :

`abduco`

- Rejoint une session, la crée si elle n'existe pas :

`abduco -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash</span>

- Rejoint une session avec `dvtm`, la crée si elle n'existe pas :

`abduco -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Quitte la session courante :

`Ctrl + \`

- Rejoint une session en mode lecture seule :

`abduco -Ar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
