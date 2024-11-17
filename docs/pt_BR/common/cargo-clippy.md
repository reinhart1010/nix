---
layout: page
title: common/cargo-clippy (português (Brasil))
description: "Conjunto de validadores para identificar erros comuns e melhorar código em Rust."
content_hash: b3ce590d5872c857ec313fb44a2dd7c32cac00b0
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/cargo-clippy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo-clippy.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-clippy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-clippy.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo clippy

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

- Executa verificações para um grupo de validadores (veja <https://rust-lang.github.io/rust-clippy/stable/index.html#?groups=cargo,complexity,correctness,deprecated,nursery,pedantic,perf,restriction,style,suspicious>):

`cargo clippy -- --warn clippy::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_validadores</span>

- Executa validações tratando avisos como erros:

`cargo clippy -- --deny warnings`

- Executa verificações e ignora avisos:

`cargo clippy -- --allow warnings`

- Aplica automaticamente as sugestões do Clippy:

`cargo clippy --fix`
