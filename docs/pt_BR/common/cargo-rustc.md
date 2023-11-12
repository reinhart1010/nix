---
layout: page
title: common/cargo-rustc (português (Brasil))
description: "Compila um pacote Rust."
content_hash: afff248473d2aa11ad29c2f519d6e830427950d2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cargo-rustc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-rustc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo rustc

Compila um pacote Rust.
Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- Compilar o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório de trabalho atual:

`cargo rustc`

- Compilar os artefatos em modo de publicação (release), com otimizações:

`cargo rustc --release`

- Compilar com otimizações específicas para a arquitetura do CPU atual:

`cargo rustc --release -- -C target-cpu=native`

- Compilar com otimização de velocidade:

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>

- Compilar com otimização de tamanho (`z` também desativa a vetorização de ciclos):

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|z</span>

- Verificar se o pacote usa código com padrões inseguros de acesso à memória:

`cargo rustc --lib -- -D unsafe-code`

- Compilar um pacote específico:

`cargo rustc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Compilar apenas o binário especificado:

`cargo --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
