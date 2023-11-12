---
layout: page
title: common/compgen (português (Brasil))
description: "Um programa para auto completar comandos no Bash, ele é executado ao pressionar duas vezes a tecla TAB."
content_hash: 9bef3ff9b3f0b1425fe7fdb7241d5e022b958bf3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/compgen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/compgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# compgen

Um programa para auto completar comandos no Bash, ele é executado ao pressionar duas vezes a tecla TAB.
Mais informações: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- Exibir todos os comandos que você pode executar:

`compgen -c`

- Exibir todos os alias:

`compgen -a`

- Exibir todas as funções que você pode executar:

`compgen -A function`

- Exibir todas as palavras reservadas do shell:

`compgen -k`

- Exibir todos os comandos/alias que iniciam com o termo 'ls':

`compgen -ac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>
