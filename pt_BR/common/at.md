---
layout: page
title: common/at (português (Brasil))
description: "Ferramenta para o agendamento de comandos."
content_hash: a1a4b075df26c54d49af248768462e155639c8b2
related_topics:
  - title: English version
    url: /en/common/at.html
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
---
# at

Ferramenta para o agendamento de comandos.
O serviço atd (ou atrun) deve estar sendo executado para as atuais execuções.
Mais informações: <https://man.archlinux.org/man/at.1>.

- Executar comandos da standard input em 5 minutos (pressionar `Ctrl + D`quando acabar):

`at now + `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` minutes`

- Executar um comando da standard input às 10:00 da manhã de hoje:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./comando.sh</span>`" | at 1000`

- Executar comandos de um dado arquivo na próxima terça:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` 9:30 PM Tue`
