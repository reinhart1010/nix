---
layout: page
title: osx/as (português (Brasil))
description: "Montador (assembler) GNU portável."
content_hash: 67a62020be7a665083c0f2c80f8f834f09f4f0d9
related_topics:
  - title: English version
    url: /en/osx/as.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/as.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/as.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># as

Montador (assembler) GNU portável.
Principalmente destinado a montar a saída do `gcc` para ser usada pelo `ld`.
Mais informações: <https://www.unix.com/man-page/osx/1/as/>.

- Montar (compilar) um arquivo, escrevendo a saída para `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>

- Montar a saída para um determinado arquivo:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saida.o</span>

- Gerar saída mais rapidamente ignorando espaços em branco e pré-processamento de comentários. (Só deve ser usado para compiladores confiáveis)

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>

- Incluir um determinado caminho na lista de diretórios para pesquisar os arquivos especificados nas diretivas `.include`:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>
