---
layout: page
title: osx/as (português (Brasil))
description: "Montador (assembler) GNU portável."
content_hash: f4e2f970fb2465c320933d7cccd3c2d9ca7a7ada
last_modified_at: 2024-01-31
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
Mais informações: <https://keith.github.io/xcode-man-pages/as.1.html>.

- Monta (compilar) um arquivo, escrevendo a saída para `a.out`:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>

- Monta a saída para um determinado arquivo:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">saida.o</span>

- Gera saída mais rapidamente ignorando espaços em branco e pré-processamento de comentários. (Só deve ser usado para compiladores confiáveis):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>

- Inclui um determinado caminho na lista de diretórios para pesquisar os arquivos especificados nas diretivas `.include`:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.s</span>
