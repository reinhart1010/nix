---
layout: page
title: common/cargo-clippy (português (Brasil))
description: "Conjunto de validadores para identificar erros comuns e melhorar código em Rust."
content_hash: fda6a954bcc4b3949a871743e298b1fbe6d7f51e
last_modified_at: 2023-08-05
related_topics:
  - title: English version
    url: /en/common/cargo-clippy.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-clippy.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo clippy

Conjunto de validadores para identificar erros comuns e melhorar código em Rust.
Mais informações: <https://github.com/rust-lang/rust-clippy>.

- Executar verificações no código no diretório atual:

`cargo clippy`

- Executar verificações garantindo que o `Cargo.lock` esteja atualizado:

`cargo clippy --locked`

- Executar verificações em todos os pacotes no workspace:

`cargo clippy --workspace`

- Executar verificações para um pacote específico:

`cargo clippy --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Executar validações tratando avisos como erros:

`cargo clippy -- --deny warnings`

- Executar verificações e ignorar avisos:

`cargo clippy -- --allow warnings`

- Aplicar automaticamente as sugestões do Clippy:

`cargo clippy --fix`
