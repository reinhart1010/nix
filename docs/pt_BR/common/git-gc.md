---
layout: page
title: common/git-gc (português (Brasil))
description: "Otimiza o repositório local limpando os arquivos desnecessários."
content_hash: 6aed2e84b6b6b26ec14b200bd2611396763f155a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/git-gc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-gc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-gc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-gc.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-gc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git gc

Otimiza o repositório local limpando os arquivos desnecessários.
Mais informações: <https://git-scm.com/docs/git-gc>.

- Otimiza o repositório:

`git gc`

- Otimiza de forma mais agressiva, demora mais tempo:

`git gc --aggressive`

- Não remove objetos perdidos (por default é removido):

`git gc --no-prune`

- Não exibe a saída:

`git gc --quiet`

- Exibe toda a ajuda:

`git gc --help`
