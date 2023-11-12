---
layout: page
title: osx/xcodes (português (Brasil))
description: "Baixe, instale e gerencie várias versões do Xcode."
content_hash: 572f69b7718c15543fef54f895f10483e37aa334
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/xcodes.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/xcodes.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xcodes

Baixe, instale e gerencie várias versões do Xcode.
Veja também: `xcodes runtimes`.
Mais informações: <https://github.com/xcodesorg/xcodes>.

- Lista todas as versões do Xcode instaladas:

`xcodes installed`

- Lista todas as versões do Xcode disponíveis:

`xcodes list`

- Seleciona uma versão do Xcode especificando o número da versão ou um caminho:

`xcodes select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao-do-xcode|caminho/para/Xcode.app</span>

- Baixa e instala uma versão específica do Xcode:

`xcodes install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao-do-xcode</span>

- Baixa, instala e seleciona a versão mais recente do Xcode:

`xcodes install --latest --select`

- Baixa uma versão específica do Xcode para um diretório específico sem instalá-la:

`xcodes download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versao-do-xcode</span>` --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>
