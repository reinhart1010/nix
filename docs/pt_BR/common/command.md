---
layout: page
title: common/command (português (Brasil))
description: "Obriga o shell a executar o programa, ignorando qualquer função ou alias com o mesmo nome."
content_hash: 3c4549bb5f91d2f0019a543e532b5bbc974cd8fc
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/command.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/command.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/command.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/command.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/command.html
    icon: bi bi-globe
tldri18n_status: 2
---
# command

Obriga o shell a executar o programa, ignorando qualquer função ou alias com o mesmo nome.
Mais informações: <https://manned.org/command>.

- Executa o programa ls, mesmo que exista algum alias ls:

`command `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- Exibe o caminho para o executável ou a definição do apelido de um comando específico:

`command -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>
