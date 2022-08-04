---
layout: page
title: common/brew (português (Brasil))
description: "A versão Linux do gerenciador de pacotes Homebrew."
content_hash: b69c66b1a2f52815fb0d8423bd6304e2028b4246
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
---
# brew

A versão Linux do gerenciador de pacotes Homebrew.
Mais informações: <https://brew.sh>.

- Buscar por fórmulas disponíveis:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termo_da_busca</span>

- Instalar a última versão estável de uma fórmula (utilizar `--devel` para versões de desenvolvimento):

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Listar as fórmulas instaladas:

`brew list`

- Atualizar uma fórmula instalada (se não for informado o nome de uma fórmula, todas as fórmulas serão atualizadas):

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Recuperar a versão mais recente do Linuxbrew e de todas as fórmulas do GitHub:

`brew update`

- Exibir as fórmulas que possuem novas versões disponíveis:

`brew outdated`

- Exibir informações sobre uma fórmula (versão, caminho de instalação, dependências, etc.):

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Verificar a instalação local em busca de possíveis problemas:

`brew doctor`
