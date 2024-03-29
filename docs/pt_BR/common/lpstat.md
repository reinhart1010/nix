---
layout: page
title: common/lpstat (português (Brasil))
description: "Exibe informações sobre o estado de impressoras."
content_hash: 06f394c0b3353f1a3b79dd5a90dd8f8e27e8ec2e
last_modified_at: 2023-12-30
related_topics:
  - title: Deutsch version
    url: /de/common/lpstat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lpstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lpstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpstat

Exibe informações sobre o estado de impressoras.
Mais informações: <https://manned.org/lpstat>.

- Lista impressoras presentes na máquina e se estão habilitadas para impressão:

`lpstat -p`

- Exibe a impressora padrão:

`lpstat -d`

- Exibe todas as informações de estado disponíveis:

`lpstat -t`

- Mostra uma lista de trabalhos de impressão que foram colocados na fila por um usuário específico:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>
