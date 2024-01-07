---
layout: page
title: common/cargo (português (Brasil))
description: "Gerencia projetos Rust e as dependências dos modulos (crates)."
content_hash: ab7c968df0955c4e5fe4439b8f980a517960f04c
last_modified_at: 2024-01-07
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
  - title: français version
    url: /fr/common/cargo.html
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
tldri18n_status: 2
---
# cargo

Gerencia projetos Rust e as dependências dos modulos (crates).
Alguns subcomandos como `cargo build` tem a sua própria documentação.
Mais informações: <https://doc.rust-lang.org/cargo>.

- Procura por crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string_procurada</span>

- Instala uma crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_crate</span>

- Lista as crates instaladas:

`cargo install --list`

- Cria um novo binário ou projeyo Rust de biblioteca no diretório especificado (ou o diretório atual por padrão):

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Adiciona uma dependência ao Cargo.toml no diretório atual:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>

- Constrói o projeto Rust no diretório atual usando o perfil de lançamento:

`cargo build --release`

- Constrói o projeto Rust no diretório atual utilizando o nightly compilador:

`cargo +nightly build`

- Constrói o projeto Rust utilizando um número específico de threads (padrão é o número de cores do CPU):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_de_threads</span>
