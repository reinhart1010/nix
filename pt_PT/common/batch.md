---
layout: page
title: common/batch (português (Portugal))
description: "Executar comandos num momento mais tarde quando a carga do sistema permitir."
content_hash: 2c024b94b407b34b01b1cd715f16f776d4d3d6bd
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
---
# batch

Executar comandos num momento mais tarde quando a carga do sistema permitir.
O serviço atd (ou atrun) deve correr para atuais execuções.
Mais informações: <https://man.archlinux.org/man/at.1>.

- Executar comandos da entrada padrão (premir `Ctrl + D` quando terminado):

`batch`

- Executar um comando da entrada padrão:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./criar_copia_bd.sh</span>`" | batch`

- Executar comandos de um dado ficheiro:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/ficheiro</span>
