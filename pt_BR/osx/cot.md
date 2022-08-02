---
layout: page
title: osx/cot (português (Brasil))
description: "Editor de texto puro para macOS."
content_hash: f63cb446d4a6afe7ef622d5549c4cfb46b51e3ce
related_topics:
  - title: English version
    url: /en/osx/cot.html
    icon: bi bi-globe
---
# cot

Editor de texto puro para macOS.
Mais informações: <https://coteditor.com/>.

- Inicia o CotEditor:

`cot`

- Abre arquivos específicos:

`cot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>

- Abre um novo documento em branco:

`cot --new`

- Abre um arquivo específico e bloqueia o terminal até que o arquivo seja fechado:

`cot --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Abre um arquivo específico com o cursor em uma linha e coluna especificada:

`cot --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_da_linha</span>` --column `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_da_coluna</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
