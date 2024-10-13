---
layout: page
title: common/passwd (português (Brasil))
description: "Passwd é uma ferramenta usada para alterar a senha de um usuário."
content_hash: 24c1ef8e5421039ce1a0bd67ae4e5718f08f0a5d
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/passwd.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/passwd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/passwd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# passwd

Passwd é uma ferramenta usada para alterar a senha de um usuário.
Mais informações: <https://manned.org/passwd>.

- Altera a senha do usuário atual interativamente:

`passwd`

- Altera a senha de um usuário específico:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome do usuário</span>

- Obtém o status atual do usuário:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-S|--status</span>

- Deixa a senha da conta em branco (isso definirá a conta nomeada como sem senha):

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>
