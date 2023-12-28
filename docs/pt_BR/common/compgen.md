---
layout: page
title: common/compgen (português (Brasil))
description: "Um programa para auto completar comandos no Bash, ele é executado ao pressionar duas vezes a tecla TAB."
content_hash: 99b67e1d06eed7f7a37978f7217deb2f2b5c021a
last_modified_at: 2023-12-28
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

- Exibe todos os comandos que você pode executar:

`compgen -c`

- Exibe todos os alias:

`compgen -a`

- Exibe todas as funções que você pode executar:

`compgen -A function`

- Exibe todas as palavras reservadas do shell:

`compgen -k`

- Exibe todos os comandos/alias que iniciam com o termo 'ls':

`compgen -ac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>
