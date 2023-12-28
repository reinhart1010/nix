---
layout: page
title: common/autossh (português (Brasil))
description: "Executa, monitora e reinicia conexões SSH."
content_hash: efc17410535ece2c3ad06f6114bfdd155b1ad66c
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/autossh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/autossh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autossh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autossh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/autossh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autossh

Executa, monitora e reinicia conexões SSH.
Reconecta automaticamente para manter os túneis de redirecionamento de porta ativos. Aceita todas as flags do `ssh`.
Mais informações: <https://www.harding.motd.ca/autossh>.

- Inicia uma sessão SSH, reiniciando quando uma porta de monitoramento falhar em retornar dados:

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_de_monitoramento</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>`"`

- Redireciona uma porta local para uma porta remota, reiniciando quando necessário:

`autossh -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_de_monitoramento</span>` -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_local</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_remota</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Executa o `autossh` em segundo plano antes de executar o `ssh` e não abrir um shell remoto:

`autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_de_monitoramento</span>` -N "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>`"`

- Executa em segundo plano, sem porta de monitoramento, e em vez disso envia pacotes de keep-alive SSH a cada 10 segundos para detectar falhas:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>`"`

- Executa em segundo plano, sem porta de monitoramento e sem shell remoto, saindo se a redireção da porta falhar:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_local</span>`:localhost:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_remota</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>

- Executa em segundo plano, registrando a saída de depuração do `autossh` e a saída detalhada do `ssh` em arquivos:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_log_do_autossh.log</span>` autossh -f -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta_de_monitoramento</span>` -v -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_log_do_ssh.log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando_ssh</span>
