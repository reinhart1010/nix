---
layout: page
title: common/renice (português (Brasil))
description: "Altera a prioridade/agradabilidade de agendamento de um ou mais processos em execução."
content_hash: f05c0f85a2dbe2e7fc45761508f77bf557eb7cf1
last_modified_at: 2024-01-13
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

- Altera a prioridade de um [p]rocesso em execução:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Altera a prioridade de todos os processos pertencentes a um [u]suário:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Altera a prioridade de todos os processos que pertencem a um [g]rupo de processos:

`renice -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_processos</span>
