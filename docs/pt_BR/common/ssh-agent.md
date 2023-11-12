---
layout: page
title: common/ssh-agent (português (Brasil))
description: "Iniciar um processo do Agente SSH."
content_hash: 17047fa647fd3227d15fd3c5d571dc8173a2a706
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-agent.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-agent.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-agent.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-agent

Iniciar um processo do Agente SSH.
Um Agente SSH mantém as chaves SSH descriptografadas na memória até serem removidas ou o processo ser encerrado.
Veja também `ssh-add`, que pode adicionar e gerenciar chaves mantidas por um Agente SSH.
Mais informações: <https://man.openbsd.org/ssh-agent>.

- Iniciar um Agente SSH para o shell atual:

`eval $(ssh-agent)`

- Encerrar o Agente em execução atualmente:

`ssh-agent -k`
