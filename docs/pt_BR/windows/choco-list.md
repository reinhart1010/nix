---
layout: page
title: windows/choco-list (português (Brasil))
description: "Exibir uma lista de pacotes com Chocolatey."
content_hash: 94a69058bd438be5e510c0733d470cca017b68fc
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
---
# choco list

Exibir uma lista de pacotes com Chocolatey.
Mais informações: <https://chocolatey.org/docs/commands-list>.

- Exibir todos pacotes disponíveis:

`choco list`

- Exibir todos pacotes instalados localmente:

`choco list --local-only`

- Exibir uma lista incluindo programas locais:

`choco list --include-programs`

- Exibir apenas pacotes aprovados:

`choco list --approved-only`

- Especificar uma fonte personalizada para exibir os pacotes:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_da_fonte|apelido</span>

- Fornecer um nome e uma senha para autenticação:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>
