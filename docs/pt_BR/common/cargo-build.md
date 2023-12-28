---
layout: page
title: common/cargo-build (português (Brasil))
description: "Compila um projeto Rust em um pacote local incluindo todas as suas dependências."
content_hash: f2cc458612087df420291e2c307665ef70501abb
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/cargo-build.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo build

Compila um projeto Rust em um pacote local incluindo todas as suas dependências.
Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compila o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório local:

`cargo build`

- Compila os artefatos em modo de publicação (release), com otimizações:

`cargo build --release`

- Compila um pacote garantindo que o `Cargo.lock` esteja atualizado:

`cargo build --locked`

- Compila todos os pacotes no workspace:

`cargo build --workspace`

- Compila um pacote específico:

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Compila apenas o binário especificado:

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Compila apenas um teste específico:

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_teste</span>
