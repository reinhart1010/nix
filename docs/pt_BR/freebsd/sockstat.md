---
layout: page
title: freebsd/sockstat (português (Brasil))
description: "Lista sockets de domínio aberto Internet ou UNIX."
content_hash: acb6ee9533e2c108df6930fb35e91a09b4b41cf1
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/freebsd/sockstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/sockstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/sockstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sockstat

Lista sockets de domínio aberto Internet ou UNIX.
Mais informações: <https://man.freebsd.org/cgi/man.cgi?sockstat>.

- Vê quais usuários/processos estão [e]scutando em quais portas:

`sockstat -l`

- Exibe informação para sockets IPv[4] e IPv[6] escutando em portas específicas usando um [p]rotocolo específico:

`sockstat -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4|6</span>` -l -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp|udp|sctp|divert</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port1,port2...</span>

- Exibe também sockets [c]onectados, não resolvendo UIDs [n]uméricos para nome de usuários e usando um campo mais largo:

`sockstat -cnw`

- Exibe somente sockets que pertencem a um ID [j]ail específico ou nome de modo detalhado:

`sockstat -jv`

- Exibe o estado do protocolo e o número da porta do encapsulamento [U]DP remoto, se aplicável (atualmente, estes estão implementados somente para SCTP e TCP):

`sockstat -sU`

- Exibe o módulo de controle de [c]ongestionamento e a pilha de protocolo, se aplicável (atualmente, estes estão implementados somente para TCP):

`sockstat -CS`

- Exibe apenas sockets da Internet se os endereços local e estrangeiro não estiverem no prefixo de rede loopback 127.0.0.0/8, ou não contiverem o endereço de loopback IPv6 ::1:

`sockstat -L`

- Não exibe o cabeçalho (modo silencioso), mostrando sockets [u]nix e exibindo o `inp_gencnt`:

`sockstat -qui`
