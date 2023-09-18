---
layout: page
title: common/sshd (português (Brasil))
description: "Daemon do Secure Shell - permite que máquinas remotas façam login de forma segura na máquina atual."
content_hash: eedd16c5cdbc99fd457a9bfb0b177d78b0603329
last_modified_at: 2023-09-18
related_topics:
  - title: English version
    url: /en/common/sshd.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sshd

Daemon do Secure Shell - permite que máquinas remotas façam login de forma segura na máquina atual.
Máquinas remotas podem executar comandos como se estivessem sendo executados nesta máquina.
Mais informações: <https://man.openbsd.org/sshd>.

- Iniciar o daemon em segundo plano:

`sshd`

- Executar o sshd em primeiro plano:

`sshd -D`

- Executar com saída detalhada (para depuração):

`sshd -D -d`

- Executar em uma porta específica:

`sshd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>
