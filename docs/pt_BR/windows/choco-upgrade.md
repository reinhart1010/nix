---
layout: page
title: windows/choco-upgrade (português (Brasil))
description: "Atualizar um ou mais pacotes com Chocolatey."
content_hash: 40c7b3c8d370ff9c0cad6079fcf7bcde6511c5ff
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-upgrade.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco upgrade

Atualizar um ou mais pacotes com Chocolatey.
Mais informações: <https://chocolatey.org/docs/commands-upgrade>.

- Atualizar um ou mais pacotes separados por espaço:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote(s)</span>

- Atualizar para uma versão específica de um pacote:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Atualizar todos pacotes:

`choco upgrade all`

- Atualizar todos os pacotes, exceto os especificados separados por virgula:

`choco upgrade all --except "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote(s)</span>`"`

- Confirmar todos prompts automaticamente:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --yes`

- Especifique uma fonte personalizada para receber pacotes:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_do_pacote|apelido</span>

- Fornecer um nome e uma senha para autenticação:

`choco upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuário</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>
