---
layout: page
title: common/git-add (português (Brasil))
description: "Adiciona arquivos modificados na área de preparação."
content_hash: dbe616abbfd2836bbe7329e0b34710da8b1a8441
last_modified_at: 2024-06-20
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-add.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git add

Adiciona arquivos modificados na área de preparação.
Mais informações: <https://git-scm.com/docs/git-add>.

- Adiciona um arquivo na área de preparação:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/do/arquivo</span>

- Adiciona todos arquivos (rastreados ou não):

`git add -A`

- Adiciona apenas arquivos rastreados:

`git add -u`

- Adiciona arquivos ignorados:

`git add -f`

- Interativamente adiciona partes dos arquivo:

`git add -p`

- Interativamente adiciona partes de um dado arquivo:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Interativamente adiciona arquivos ou partes modificadas:

`git add -i`
