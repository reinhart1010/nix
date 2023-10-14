---
layout: page
title: common/passwd (português (Brasil))
description: "Passwd é uma ferramenta usada para alterar a senha de um usuário."
content_hash: 2814993806242a951c03713780519d37a6948543
last_modified_at: 2023-10-14
related_topics:
  - title: English version
    url: /en/common/passwd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/passwd.html
    icon: bi bi-globe
---
# passwd

Passwd é uma ferramenta usada para alterar a senha de um usuário.
Mais informações: <https://manned.org/passwd>.

- Altera a senha do usuário atual interativamente:

`passwd`

- Altera a senha de um usuário específico:

`passwd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome do usuário</span>

- Obtém o status atual do usuário:

`passwd -S`

- Deixa a senha da conta em branco (isso definirá a conta nomeada como sem senha):

`passwd -d`
