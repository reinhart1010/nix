---
layout: page
title: linux/chage (português (Brasil))
description: "Gerencia informações de expiração de conta e senha do usuário."
content_hash: 5996abcdbacfab90a65f9ff4a7ddb5102b7b8e24
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/chage.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/chage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chage

Gerencia informações de expiração de conta e senha do usuário.
Mais informações: <https://manned.org/chage>.

- Exibe as informações referentes a senha do usuário:

`chage --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Habilita a expiração da senha do usuário em 10 dias:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Desabilita a expiração da senha do usuário:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Define a data de expiração da conta do usuário:

`sudo chage --expiredate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Obriga o usuário a alterar sua senha no próximo login:

`sudo chage --lastday `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>
