---
layout: page
title: common/batch (português (Portugal))
description: "Executar comandos num momento mais tarde quando a carga do sistema permitir."
content_hash: 714a50da95ea987ba910c7589c90ee1154338876
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/batch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# batch

Executar comandos num momento mais tarde quando a carga do sistema permitir.
O serviço atd (ou atrun) deve correr para atuais execuções.
Mais informações: <https://manned.org/batch>.

- Executa comandos da entrada padrão (premir `Ctrl + D` quando terminado):

`batch`

- Executa um comando da entrada padrão:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./criar_copia_bd.sh</span>`" | batch`

- Executa comandos de um dado ficheiro:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ficheiro</span>
