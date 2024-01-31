---
layout: page
title: osx/codesign (português (Brasil))
description: "Cria e manipula assinaturas de código para macOS."
content_hash: 9b32b9511403e10d3ef41dd27580a46b49c992fc
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/codesign.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/codesign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# codesign

Cria e manipula assinaturas de código para macOS.
Mais informações: <https://keith.github.io/xcode-man-pages/codesign.1.html>.

- Assina um aplicativo com um certificado:

`codesign --sign "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Nome da Minha Empresa</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/App.app</span>

- Verifica o certificado de um aplicativo:

`codesign --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/App.app</span>
