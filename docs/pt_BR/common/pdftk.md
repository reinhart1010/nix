---
layout: page
title: common/pdftk (português (Brasil))
description: "Conjunto de utilitários para manipular arquivos PDF."
content_hash: 80187c7935205ad039ae94eb032f5a7995114b48
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/pdftk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pdftk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftk

Conjunto de utilitários para manipular arquivos PDF.
Mais informações: <https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>.

- Extrai conjuntos de páginas de um arquivo PDF (páginas 1 a 3, 5 e 6 a 10) e guardá-las num novo arquivo:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3 5 6-10</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_arquivo.pdf</span>

- Concatena uma lista de arquivos PDF, guardando o resultado num novo arquivo:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo1.pdf arquivo2.pdf arquivoN.pdf ...</span>` cat output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_arquivo.pdf</span>

- Parte cada página de um arquivo PDF num arquivo separado, com um padrão para o nome dos novos arquivos:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.pdf</span>` burst output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">página_%d.pdf</span>

- Gira em 180° todas as páginas de um arquivo PDF:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-endsouth</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_arquivo.pdf</span>

- Gira a terceira página de um arquivo PDF em 90° no sentido horário, não modificando as restantes:

`pdftk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.pdf</span>` cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-2 3east 4-end</span>` output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">novo_arquivo.pdf</span>
