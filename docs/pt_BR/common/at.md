---
layout: page
title: common/at (português (Brasil))
description: "Ferramenta para o agendamento de comandos."
content_hash: af201a8e0fb7b97a8d673a4fc0624a0457627231
last_modified_at: 2024-10-17
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
  - title: Nederlands version
    url: /nl/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># at

Ferramenta para o agendamento de comandos.
O serviço atd (ou atrun) deve estar sendo executado para as atuais execuções.
Mais informações: <https://manned.org/at>.

- Executa comandos da standard input em 5 minutos (pressionar `Ctrl + D`quando acabar):

`at now + 5 minutes`

- Executa um comando da standard input às 10:00 da manhã de hoje:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./comando.sh</span>`" | at 1000`

- Executa comandos de um dado arquivo na próxima terça:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` 9:30 PM Tue`
