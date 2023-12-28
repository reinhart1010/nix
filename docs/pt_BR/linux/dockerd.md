---
layout: page
title: linux/dockerd (português (Brasil))
description: "Um processo persistente para iniciar e gerenciar contêineres Docker."
content_hash: af1180c043e720154425e3315cc4b7f0a3218ad3
last_modified_at: 2023-12-28
related_topics:
  - title: العربية version
    url: /ar/linux/dockerd.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dockerd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dockerd

Um processo persistente para iniciar e gerenciar contêineres Docker.
Mais informações: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- Executa o daemon do Docker:

`dockerd`

- Executa o daemon do Docker e configurá-lo para escutar em sockets específicos (UNIX e TCP):

`dockerd --host unix://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/tmp.sock</span>` --host tcp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>

- Executa com um arquivo PID específico para o daemon:

`dockerd --pidfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_pid</span>

- Executa no modo de depuração:

`dockerd --debug`

- Executa e define um nível de log específico:

`dockerd --log-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|info|warn|error|fatal</span>
