---
layout: page
title: linux/top (português (Brasil))
description: "Utilitário para exibir informações, em tempo real, sobre os processos em execução."
content_hash: cd777d7e9d7432ea2afbb2f246d24e8b46d6f339
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/top.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/top.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/top.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># top

Utilitário para exibir informações, em tempo real, sobre os processos em execução.
Mais informações: <https://manned.org/top>.

- Iniciar top:

`top`

- Exibir apenas os processos ativos:

`top -i`

- Exibir os processos de um usuário específico:

`top -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Exibir o(s) processo(s) de um ou mais PID específico(s), separado(s) por vírgula:

`top -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID1,PID2,PID3</span>

- Mostra Ajuda sobre os comandos disponíveis:

`?`
