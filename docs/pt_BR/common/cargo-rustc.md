---
layout: page
title: common/cargo-rustc (português (Brasil))
description: "Compila um pacote Rust."
content_hash: 1b30f46802477712ba4e8ed57fa5fcf667483079
last_modified_at: 2023-12-28
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

- Compila o pacote ou pacotes definidos pelo arquivo `Cargo.toml` no diretório de trabalho atual:

`cargo rustc`

- Compila os artefatos em modo de publicação (release), com otimizações:

`cargo rustc --release`

- Compila com otimizações específicas para a arquitetura do CPU atual:

`cargo rustc --release -- -C target-cpu=native`

- Compila com otimização de velocidade:

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>

- Compila com otimização de tamanho (`z` também desativa a vetorização de ciclos):

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|z</span>

- Verifica se o pacote usa código com padrões inseguros de acesso à memória:

`cargo rustc --lib -- -D unsafe-code`

- Compila um pacote específico:

`cargo rustc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Compila apenas o binário especificado:

`cargo --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>
