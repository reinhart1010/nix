---
layout: page
title: linux/top (português (Brasil))
description: "Utilitário para exibir informações, em tempo real, sobre os processos em execução."
content_hash: cd777d7e9d7432ea2afbb2f246d24e8b46d6f339
related_topics:
  - title: English version
    url: /en/linux/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/top.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/top.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
