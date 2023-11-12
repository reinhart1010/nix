---
layout: page
title: common/kill (português (Brasil))
description: "Envia um sinal para um processo, geralmente para finalizar o processo."
content_hash: 40d89b616c00e2e2783dc22b3c400bbf095ac8da
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/kill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kill.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kill.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kill

Envia um sinal para um processo, geralmente para finalizar o processo.
Todos os sinais exceto pelo SIGKILL e SIGSTOP podem ser interceptados pelo processo para finalizar de forma limpa.
Mais informações: <https://manned.org/kill>.

- Finaliza um programa usando o sinal default SIGTERM (terminate):

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_processo</span>

- Lista todos os nomes dos sinais disponíveis (para serem usados sem o prefixo `SIG`):

`kill -l`

- Finaliza um processo em background:

`kill %`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_processo</span>

- Finaliza um programa usando o sinal SIGHUP. Muitos daemons vão recarregar ao invés de finalizar:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_processo</span>

- Finaliza um programa usando o sinal SIGINT (interrupt). Isto é tipicamente iniciado pelo usuário ao pressionar `Ctrl + C`:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_processo</span>

- Envia sinal para o sistema operacional para finalizar imediatamente o programa (quem não tem chance de capturar o sinal):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_processo</span>

- Envia sinal para o sistema operacional para pausar o programa até um sinal SIGCONT ("continue") seja recebido:

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_processo</span>

- Envia um sinal `SIGUSR1` para todos os processos de um dado GID (group id):

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_do_grupo</span>
