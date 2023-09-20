---
layout: page
title: linux/dockerd (português (Brasil))
description: "Um processo persistente para iniciar e gerenciar contêineres Docker."
content_hash: c4a102ed092371e443143baaae5d4933d01d8485
last_modified_at: 2023-09-20
related_topics:
  - title: العربية version
    url: /ar/linux/dockerd.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dockerd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dockerd

Um processo persistente para iniciar e gerenciar contêineres Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- Executar o daemon do Docker:

`dockerd`

- Executar o daemon do Docker e configurá-lo para escutar em sockets específicos (UNIX e TCP):

`dockerd --host unix://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/tmp.sock</span>` --host tcp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- Executar com um arquivo PID específico para o daemon:

`dockerd --pidfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_pid</span>

- Executar no modo de depuração:

`dockerd --debug`

- Executar e definir um nível de log específico:

`dockerd --log-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warn|error|fatal</span>
