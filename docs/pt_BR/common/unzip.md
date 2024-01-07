---
layout: page
title: common/unzip (português (Brasil))
description: "Ferramenta de descompactação de arquivos zip."
content_hash: 677ba85d68c431ebeefdc14f45b56699cf2b4a33
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/unzip.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unzip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/unzip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unzip

Ferramenta de descompactação de arquivos zip.
Mais informações: <https://manned.org/unzip>.

- Extrai arquivos zip:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...</span>

- Extrai arquivos zip para caminhos específicos:

`unzip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/saída</span>

- Extrai arquivos/diretórios de arquivos para `stdout`:

`unzip -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...</span>

- Extrai o conteúdo do(s) arquivo(s) para `stdout` ao lado dos nomes dos arquivos extraídos:

`unzip -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gbk</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1.zip caminho/para/arquivo2.zip ...</span>

- Lista conteúdos de arquivos zip:

`unzip -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.zip</span>

- Extrai arquivos zip sem a estrutura dos diretórios:

`unzip -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo1 caminho/para/arquivo2 ...</span>
