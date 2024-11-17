---
layout: page
title: common/cargo-test (português (Brasil))
description: "Executa os testes unitários e de integração de um pacote Rust."
content_hash: 6f4f0e8f11f9ce39b1edcf60fede00fbd83f2293
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/cargo-test.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo-test.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-test.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-test.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo test

Executa os testes unitários e de integração de um pacote Rust.
Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- Executa apenas os testes que contenham um texto específico em seus nomes:

`cargo test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomedoteste</span>

- Define o número de casos de teste para execução simultânea:

`cargo test -- --test-threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quantidade</span>

- Testa os artefatos em modo de publicação (release), com otimizações:

`cargo test --release`

- Testa todos os pacotes no workspace:

`cargo test --workspace`

- Executa testes para um pacote específico:

`cargo test --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Executa testes sem ocultar a saída das execuções dos testes:

`cargo test -- --nocapture`
