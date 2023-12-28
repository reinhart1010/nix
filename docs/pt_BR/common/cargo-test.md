---
layout: page
title: common/cargo-test (português (Brasil))
description: "Executa os testes unitários e de integração de um pacote Rust."
content_hash: c405be0ff31c740cb78a36ccc074ac84d2b705f1
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/cargo-test.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-test.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo test

Executa os testes unitários e de integração de um pacote Rust.
Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Executa apenas os testes que contenham uma string específica em seus nomes:

`cargo test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomedoteste</span>

- Define o número de casos de teste para execução simultânea:

`cargo test -- --test-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quantidade</span>

- Executa os testes garantindo que o `Cargo.lock` esteja atualizado:

`cargo test --locked`

- Testa os artefatos em modo de publicação (release), com otimizações:

`cargo test --release`

- Testa todos os pacotes no workspace:

`cargo test --workspace`

- Executa testes para um pacote específico:

`cargo test --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Executa testes sem ocultar a saída das execuções dos testes:

`cargo test -- --nocapture`
