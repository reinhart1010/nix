---
layout: page
title: linux/chage (português (Brasil))
description: "Gerencia informações de expiração de conta e senha do usuário."
content_hash: fd20d6a334cfaae268824fb67131460231f48472
last_modified_at: 2023-11-12
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

- Exibir as informações referentes a senha do usuário:

`chage --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Habilitar a expiração da senha do usuário em 10 dias:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Desabilitar a expiração da senha do usuário:

`sudo chage --maxdays `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Definir a data de expiração da conta do usuário:

`sudo chage --expiredate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>

- Obrigar o usuário a alterar sua senha no próximo login:

`sudo chage --lastday `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_usuario</span>
