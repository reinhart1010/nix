---
layout: page
title: common/nano (português (Brasil))
description: "Editor de texto de linha de comando simples e fácil de usar. Um clone melhorado e gratuito de Pico."
content_hash: 16b35990b7d83b114f0f74921084ef73499eb73c
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
---
# nano

Editor de texto de linha de comando simples e fácil de usar. Um clone melhorado e gratuito de Pico.
Mais informações: <https://nano-editor.org>.

- Abre um novo arquivo no nano:

`nano`

- Abre um arquivo específico:

`nano `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo específico, posicionando o cursor na linha e coluna especificadas:

`nano +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linha</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">coluna</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo específico e habilita soft wrapping:

`nano --softwrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo específico e indenta novas linhas para a indentação das linhas anteriores:

`nano --autoindent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre nano e cria um arquivo backup (`file~`) quando salva edições:

`nano --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
