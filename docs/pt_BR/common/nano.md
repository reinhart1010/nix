---
layout: page
title: common/nano (português (Brasil))
description: "Editor de texto de linha de comando. Um clone melhorado de `Pico`."
content_hash: 7cc8441e0fb59ac1335b9dde758a76f21f399e86
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/nano.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nano.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/nano.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nano.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nano

Editor de texto de linha de comando. Um clone melhorado de `Pico`.
Mais informações: <https://nano-editor.org>.

- Inicia o editor:

`nano`

- Inicia o editor sem usar arquivos de configuração:

`nano --ignorercfiles`

- Abre arquivos específicos, passando para o próximo arquivos ao fechar o anterior:

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Abre um arquivo e posiciona o cursor na linha e coluna especificadas:

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linha</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">coluna</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo e habilita soft wrapping:

`nano --softwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo e indenta novas linhas de acordo com a indentação da linha anterior:

`nano --autoindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo e cria um arquivo de backup (`caminho/para/arquivo~`) ao salvá-lo:

`nano --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
