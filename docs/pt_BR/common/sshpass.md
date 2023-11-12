---
layout: page
title: common/sshpass (português (Brasil))
description: "Um provedor de senha SSH."
content_hash: 61145bc5604099fe6c9ee6734da5e12ca863b10c
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/sshpass.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sshpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sshpass

Um provedor de senha SSH.
Ele funciona criando um TTY, inserindo a senha nele e, em seguida, redirecionando `stdin` para a sessão SSH.
Mais informações: <https://manned.org/sshpass>.

- Conectar-se a um servidor remoto usando uma senha fornecida em um descritor de arquivo (neste caso, `stdin`):

`sshpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Conectar-se a um servidor remoto com a senha fornecida como opção e aceitar automaticamente chaves SSH desconhecidas:

`sshpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Conectar-se a um servidor remoto usando a primeira linha de um arquivo como senha, aceitar automaticamente chaves SSH desconhecidas e executar um comando:

`sshpass -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`
