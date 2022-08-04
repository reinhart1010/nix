---
layout: page
title: common/git-mv (português (Brasil))
description: "Move ou renomeia arquivos e atualiza o index do Git."
content_hash: ebf3c16cd49e8231c8cd3b05450bb19efc720ec6
related_topics:
  - title: English version
    url: /en/common/git-mv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-mv.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-mv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-mv.html
    icon: bi bi-globe
---
# git mv

Move ou renomeia arquivos e atualiza o index do Git.
Mais informações: <https://git-scm.com/docs/git-mv>.

- Move arquivos dentro de um repositório e adiciona no próximo commit:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo/caminho</span>

- Renomeia um arquivo e adiciona a renomeação no próximo commit:

`git mv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_nome</span>

- Sobrescreve o arquivo no caminho alvo se ele já existir:

`git mv --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alvo</span>
