---
layout: page
title: common/ack (português (Brasil))
description: "Uma ferramenta de pesquisa similar ao `grep`, otimizada para programadores."
content_hash: eebc1517e6973d955209fda4e9d2a21589b6d441
last_modified_at: 2024-11-18
related_topics:
  - title: বাংলা version
    url: /bn/common/ack.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ack.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ack.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ack.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ack.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ack.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ack.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ack.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ack.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ack.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ack.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ack.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ack

Uma ferramenta de pesquisa similar ao `grep`, otimizada para programadores.
Veja também: `rg`, que é muito mais rápido.
Mais informações: <https://beyondgrep.com/documentation>.

- Procura por arquivos que contenham o termo, ou a expressão regular, no diretório atual:

`ack "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_de_busca</span>`"`

- Procura um padrão sem diferenciar maiúsculas e minúsculas:

`ack --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_de_busca</span>`"`

- Procura por linhas correspondentes ao padrão, imprimindo apenas o texto correspondente e não o resto da linha:

`ack -o "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_de_busca</span>`"`

- Limita a busca a um tipo específico de arquivo:

`ack --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_de_busca</span>`"`

- Não busca arquivos de um tipo específico:

`ack --type no`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruby</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_de_busca</span>`"`

- Conta o total de correspondências encontradas:

`ack --count --no-filename "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_de_busca</span>`"`

- Imprime o nome dos arquivos e o número de correspondências para cada arquivo:

`ack --count --files-with-matches "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_de_busca</span>`"`

- Lista todos os valores que podem ser utilizados com `--type`:

`ack --help-types`
