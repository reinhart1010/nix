---
layout: page
title: common/renice (português (Brasil))
description: "Altera a prioridade/agradabilidade de agendamento de um ou mais processos em execução."
content_hash: 726a95beb0c2d9d52b9bc49ece6b452444c16f90
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/renice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# renice

Altera a prioridade/agradabilidade de agendamento de um ou mais processos em execução.
Os valores de agradabilidade variam de -20 (mais favorável ao processo) a 19 (menos favorável ao processo).
Mais informações: <https://manned.org/renice>.

- Altera a prioridade de um processo em execução:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_de_agradabilidade</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Altera a prioridade de todos os processos pertencentes a um usuário:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_de_agradabilidade</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Altera a prioridade de todos os processos que pertencem a um grupo de processos:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_de_agradabilidade</span>` --pgrp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_processos</span>
