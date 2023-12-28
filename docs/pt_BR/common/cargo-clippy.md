---
layout: page
title: common/cargo-clippy (português (Brasil))
description: "Conjunto de validadores para identificar erros comuns e melhorar código em Rust."
content_hash: 28bb1cb95d1b7408e1d35125e52ae1c1450da0b8
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/cargo-clippy.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-clippy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo clippy

Conjunto de validadores para identificar erros comuns e melhorar código em Rust.
Mais informações: <https://github.com/rust-lang/rust-clippy>.

- Executa verificações no código no diretório atual:

`cargo clippy`

- Executa verificações garantindo que o `Cargo.lock` esteja atualizado:

`cargo clippy --locked`

- Executa verificações em todos os pacotes no workspace:

`cargo clippy --workspace`

- Executa verificações para um pacote específico:

`cargo clippy --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Executa validações tratando avisos como erros:

`cargo clippy -- --deny warnings`

- Executa verificações e ignora avisos:

`cargo clippy -- --allow warnings`

- Aplica automaticamente as sugestões do Clippy:

`cargo clippy --fix`
