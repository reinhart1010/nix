---
layout: page
title: common/dvc-add (português (Brasil))
description: "Adiciona um arquivo modificado para o índice."
content_hash: 15cc6c6828f110e21ff3b69f87b91479f51e8a15
last_modified_at: 2023-10-08
related_topics:
  - title: English version
    url: /en/common/dvc-add.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dvc add

Adiciona um arquivo modificado para o índice.
Mais informações: <https://dvc.org/doc/command-reference/add>.

- Adiciona um arquivo para o índice:

`dvc add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Adiciona um diretório para o índice:

`dvc add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Adiciona recursivamente todos os arquivos em um dado diretório:

`dvc add --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Adiciona um arquivo com o nome `.dvc` customizado:

`dvc add --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_customizado.dvc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
