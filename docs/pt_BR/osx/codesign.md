---
layout: page
title: osx/codesign (português (Brasil))
description: "Cria e manipula assinaturas de código para macOS."
content_hash: 74504f53b905ae0f46b4ba6bc88325f2f2977c84
related_topics:
  - title: English version
    url: /en/osx/codesign.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/codesign.html
    icon: bi bi-globe
---
# codesign

Cria e manipula assinaturas de código para macOS.
Mais informações: <https://www.unix.com/man-page/osx/1/codesign/>.

- Assina um aplicativo com um certificado:

`codesign --sign "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Nome da Minha Empresa</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/App.app</span>

- Verifica o certificado de um aplicativo:

`codesign --verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/App.app</span>
