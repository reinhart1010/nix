---
layout: page
title: common/finger (português (Brasil))
description: "Programa de pesquisa de informações do usuário."
content_hash: 2fed5d4e474f1d65f03baf6089288296c58ede88
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/finger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# finger

Programa de pesquisa de informações do usuário.
Mais informações: <https://manned.org/finger>.

- Exibe informações sobre usuários conectados no momento:

`finger`

- Exibe informações sobre um usuário específico:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_de_usuário</span>

- Exibe o nome de login do usuário, nome real, nome do terminal e outras informações:

`finger -s`

- Produz o formato de saída de várias linhas exibindo as mesmas informações que `-s`, bem como o diretório pessoal do usuário, número de telefone residencial, shell de login, status de correio, etc.:

`finger -l`

- Impede a correspondência com os nomes de usuário e usa apenas nomes de login:

`finger -m`
