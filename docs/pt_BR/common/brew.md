---
layout: page
title: common/brew (português (Brasil))
description: "A versão Linux do gerenciador de pacotes Homebrew."
content_hash: 1e468dabe9789a6007997e1882d76a9c72a0b96a
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew

A versão Linux do gerenciador de pacotes Homebrew.
Mais informações: <https://docs.brew.sh/Manpage>.

- Busca por fórmulas disponíveis:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termo_da_busca</span>

- Instala a última versão estável de uma fórmula (utilizar `--devel` para versões de desenvolvimento):

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Lista as fórmulas instaladas:

`brew list`

- Atualiza uma fórmula instalada (se não for informado o nome de uma fórmula, todas as fórmulas serão atualizadas):

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Recupera a versão mais recente do Linuxbrew e de todas as fórmulas do GitHub:

`brew update`

- Exibe as fórmulas que possuem novas versões disponíveis:

`brew outdated`

- Exibe informações sobre uma fórmula (versão, caminho de instalação, dependências, etc.):

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Verifica a instalação local em busca de possíveis problemas:

`brew doctor`
