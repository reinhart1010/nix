---
layout: page
title: osx/carthage (português (Brasil))
description: "Ferramenta de gerenciamento de dependências para aplicativos Cocoa."
content_hash: e0552b3842c4b3e1c3beb5fb90b0c628ccf87b45
related_topics:
  - title: English version
    url: /en/osx/carthage.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/carthage.html
    icon: bi bi-globe
---
# carthage

Ferramenta de gerenciamento de dependências para aplicativos Cocoa.
Mais informações: <https://github.com/Carthage/Carthage>.

- Baixa a versão mais recente de todas as dependências mencionadas no Cartfile e realiza o build delas:

`carthage update`

- Atualiza as dependências, e faz build apenas para o iOS:

`carthage update --platform ios`

- Atualiza as dependências, sem realizar build de nenhuma delas:

`carthage update --no-build`

- Faz o download e rebuild da versão atual das dependências (sem atualizá-las):

`carthage bootstrap`

- Faz o rebuild de uma dependência específica:

`carthage build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>
