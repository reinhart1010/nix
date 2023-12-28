---
layout: page
title: common/sshpass (português (Brasil))
description: "Um provedor de senha SSH."
content_hash: ba1d66819e239656bf6b411daab5b8177a89c356
last_modified_at: 2023-12-28
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

- Conecta a um servidor remoto usando uma senha fornecida em um descritor de arquivo (neste caso, `stdin`):

`sshpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Conecta a um servidor remoto com a senha fornecida como opção e aceita automaticamente chaves SSH desconhecidas:

`sshpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Conecta a um servidor remoto usando a primeira linha de um arquivo como senha, aceita automaticamente chaves SSH desconhecidas e executa um comando:

`sshpass -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>` ssh -o StrictHostKeyChecking=no `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`
