---
layout: page
title: common/ag (français)
description: "The Silver Searcher. Comme ack, mais inspire à être plus rapide."
content_hash: 4fcb1a0d4b8331aef1578e51a66a3d3f114a03dc
related_topics:
  - title: English version
    url: /en/common/ag.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ag.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ag.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ag.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ag.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ag.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ag

The Silver Searcher. Comme ack, mais inspire à être plus rapide.
Plus d'informations : <https://github.com/ggreer/the_silver_searcher>.

- Trouve les fichiers qui contiennent "foo", et affiche les lignes correspondantes dans le contexte courant :

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Trouve les fichiers qui contiennent "foo" dans un dossier spécifique :

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chelin/vers/dossier</span>

- Trouve les fichiers qui contiennent "foo", mais affiche les nom de fichier uniquement :

`ag -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Trouve les fichiers qui contiennent "FOO" en étant insensible à la casse et affiche que le premier résultat plutôt que la ligne entière :

`ag -i -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FOO</span>

- Trouve "foo" dans les fichiers avec un nom contenant "bar" :

`ag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` -G `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Trouve des fichiers dont le contenu correspond à une expression régulière :

`ag '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">^ba(r|z)$</span>`'`

- Trouve les fichiers avec un nom contenant "foo" :

`ag -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>
