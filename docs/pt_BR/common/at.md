---
layout: page
title: common/at (português (Brasil))
description: "Ferramenta para o agendamento de comandos."
content_hash: fe5ec803489c8cc9cf18df8dc088f70d01697e34
last_modified_at: 2024-10-25
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
tldri18n_status: 2
---
# at

Ferramenta para o agendamento de comandos.
Resultados serão enviados para o e-mail dos usuários.
Mais informações: <https://manned.org/at>.

- Inicia o daemon `atd`:

`systemctl start atd`

- Cria comandos interativamente e executa-os em 5 minutos (pressione `<Ctrl> + D` quando acabar):

`at now + 5 minutes`

- Cria comandos interativamente e executa-os no horário específico:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hh:mm</span>

- Executa um comando da `stdin` (standard input) às 10:00 da manhã de hoje:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`" | at 1000`

- Executa comandos de um dado arquivo na próxima terça:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` 9:30 PM Tue`
