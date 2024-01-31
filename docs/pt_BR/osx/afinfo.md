---
layout: page
title: osx/afinfo (português (Brasil))
description: "Parser de metadados de arquivos de áudio para OS X."
content_hash: 39a3c7832c0984aaa9688f122269bf698f3096a6
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/afinfo.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/afinfo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/afinfo.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/afinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# afinfo

Parser de metadados de arquivos de áudio para OS X.
Comando nativo do OS X.
Mais informações: <https://keith.github.io/xcode-man-pages/afinfo.1.html>.

- Exibe informações de um determinado arquivo de áudio:

`afinfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime uma descrição de uma linha do arquivo de áudio:

`afinfo --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime informações de metadados e conteúdo do InfoDictionary do arquivo de áudio:

`afinfo --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime saída em formato XML:

`afinfo --xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Imprime avisos para o arquivo de áudio, se houver:

`afinfo --warnings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Exibe ajuda sobre o uso completo:

`afinfo --help`
