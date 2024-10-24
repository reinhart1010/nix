---
layout: page
title: common/git-tag (português (Brasil))
description: "Cria, exibe, exclui ou verifica tags."
content_hash: cf3d0be703d7b90f188cb1d60dee2d69772f10c9
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/common/git-tag.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-tag.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-tag.html
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
  - title: Türkçe version
    url: /tr/common/git-tag.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git tag

Cria, exibe, exclui ou verifica tags.
Uma tag é uma referência estática para um commit.
Mais informações: <https://git-scm.com/docs/git-tag>.

- Exibe todas as tags:

`git tag`

- Cria uma tag com o nome fornecido apontando para o commit atual:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_tag</span>

- Cria uma tag com o nome fornecido apontando para um determinado commit:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Cria uma tag anotada com a mensagem fornecida:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_tag</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mensagem_da_tag</span>

- Exclui a tag com o nome fornecido:

`git tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_tag</span>

- Obtém tags atualizadas do remote:

`git fetch --tags`

- Envia uma tag para o remote:

`git push origin tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_tag</span>

- Lista todas as tags cujos ancestrais incluem um determinado commit:

`git tag --contains `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
