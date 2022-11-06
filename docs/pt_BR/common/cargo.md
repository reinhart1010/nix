---
layout: page
title: common/cargo (português (Brasil))
description: "Gerencia projetos Rust e as dependências dos modulos (crates)."
content_hash: fd350e366b7463776c4d929355bcd04af23c5b53
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cargo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cargo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo

Gerencia projetos Rust e as dependências dos modulos (crates).
Alguns subcomandos como `cargo build` tem a sua própria documentação.
Mais informações: <https://crates.io>.

- Procura por crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string_procurada</span>

- Instala uma crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_crate</span>

- Lista as crates instaladas:

`cargo install --list`

- Cria um projeto Rust sendo binário ou uma biblioteca no diretório atual:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Cria um projeto Rust sendo binário ou uma biblioteca em um diretório específico:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/directório</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Constrói o projeto Rust no diretório atual:

`cargo build`

- Constrói o projeto Rust no diretório atual utilizando o nightly compilador:

`cargo +nightly build`

- Constrói o projeto Rust utilizando um número específico de threads (padrão é o número de cores do CPU):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_threads</span>