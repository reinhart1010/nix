---
layout: page
title: windows/choco-install (português (Brasil))
description: "Instalar um pacote ou mais com Chocolatey."
content_hash: e51ba0cbbb5033f3dc6efa45948567f4a7511f82
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-install.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/choco-install.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-install.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-install.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco install

Instalar um pacote ou mais com Chocolatey.
Mais informações: <https://chocolatey.org/docs/commands-install>.

- Instalar um ou mais pacotes separado por espaço:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote(s)</span>

- Instalar pacotes a partir de um aquivo de configuração personalizado:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/pacotes.config</span>

- Instalar um arquivo específico `nuspec` ou `nupkg`:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Instalar uma versão específica de um pacote:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Permitir a instalação de múltiplas versões de um pacote:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --allow-multiple`

- Confirmar todos prompts automaticamente:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --yes`

- Especificar uma fonte personalizada para receber pacotes:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_do_pacote|apelido</span>

- Fornecer um nome e uma senha para autenticação:

`choco install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>` --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">senha</span>
