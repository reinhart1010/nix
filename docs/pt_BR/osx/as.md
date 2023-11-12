---
layout: page
title: osx/as (português (Brasil))
description: "Montador (assembler) GNU portável."
content_hash: efabea67866d96dbb9fd8c76ab94ef0df20a2c6a
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# as

Montador (assembler) GNU portável.
Principalmente destinado a montar a saída do `gcc` para ser usada pelo `ld`.
Mais informações: <https://www.unix.com/man-page/osx/1/as/>.

- Montar (compilar) um arquivo, escrevendo a saída para `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>

- Montar a saída para um determinado arquivo:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saida.o</span>

- Gerar saída mais rapidamente ignorando espaços em branco e pré-processamento de comentários. (Só deve ser usado para compiladores confiáveis):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>

- Incluir um determinado caminho na lista de diretórios para pesquisar os arquivos especificados nas diretivas `.include`:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>
