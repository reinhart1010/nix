---
layout: page
title: common/sshd (português (Brasil))
description: "Daemon do Secure Shell - permite que máquinas remotas façam login de forma segura na máquina atual."
content_hash: 7a9879fca4eb5e58bd3a4f674f7b0b7902612c47
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/sshd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sshd

Daemon do Secure Shell - permite que máquinas remotas façam login de forma segura na máquina atual.
Máquinas remotas podem executar comandos como se estivessem sendo executados nesta máquina.
Mais informações: <https://man.openbsd.org/sshd>.

- Inicia o daemon em segundo plano:

`sshd`

- Executa o sshd em primeiro plano:

`sshd -D`

- Executa com saída detalhada (para depuração):

`sshd -D -d`

- Executa em uma porta específica:

`sshd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>
