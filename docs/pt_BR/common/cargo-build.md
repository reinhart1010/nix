---
layout: page
title: common/cargo-build (português (Brasil))
description: "Compila um projeto Rust em um pacote local incluindo todas as suas dependências."
content_hash: 30495deec2ca2bec6cf31a64321d12c8d4951688
last_modified_at: 2023-11-12
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

- Compilar o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório local:

`cargo build`

- Compilar os artefatos em modo de publicação (release), com otimizações:

`cargo build --release`

- Compilar um pacote garantindo que o `Cargo.lock` esteja atualizado:

`cargo build --locked`

- Compilar todos os pacotes no workspace:

`cargo build --workspace`

- Compilar um pacote específico:

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Compilar apenas o binário especificado:

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Compilar apenas um teste específico:

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_teste</span>
