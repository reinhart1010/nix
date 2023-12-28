---
layout: page
title: windows/choco-list (português (Brasil))
description: "Exibir uma lista de pacotes com Chocolatey."
content_hash: 9ec9ac15bf5769e0d235f76fe2de5c674d4954ca
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/choco-list.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-list.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco list

Exibir uma lista de pacotes com Chocolatey.
Mais informações: <https://chocolatey.org/docs/commands-list>.

- Exibe todos pacotes disponíveis:

`choco list`

- Exibe todos pacotes instalados localmente:

`choco list --local-only`

- Exibe uma lista incluindo programas locais:

`choco list --include-programs`

- Exibe apenas pacotes aprovados:

`choco list --approved-only`

- Especifica uma fonte personalizada para exibir os pacotes:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_da_fonte|apelido</span>

- Fornece um nome e uma senha para autenticação:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>
