---
layout: page
title: common/at (português (Brasil))
description: "Ferramenta para o agendamento de comandos."
content_hash: eeceefb6c201edf4b8a56bd97c5422d0223f2003
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Ferramenta para o agendamento de comandos.
O serviço atd (ou atrun) deve estar sendo executado para as atuais execuções.
Mais informações: <https://manned.org/at>.

- Executar comandos da standard input em 5 minutos (pressionar `Ctrl + D`quando acabar):

`at now + `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` minutes`

- Executar um comando da standard input às 10:00 da manhã de hoje:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./comando.sh</span>`" | at 1000`

- Executar comandos de um dado arquivo na próxima terça:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` 9:30 PM Tue`
