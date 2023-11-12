---
layout: page
title: common/cargo-add (português (Brasil))
description: "Adiciona dependências ao arquivo `Cargo.toml` de um projeto Rust."
content_hash: 56c2c09338b8b4421c4c36a96589f43e5be1e45e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cargo-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo add

Adiciona dependências ao arquivo `Cargo.toml` de um projeto Rust.
Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Adicionar a versão mais recente de uma dependência ao projeto atual:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>

- Adicionar uma versão específica de uma dependência:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Adicionar uma dependência e habilitar uma ou mais funcionalidades específicas:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">funcionalidade_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">funcionalidade_2</span>

- Adicionar uma dependência opcional, que será exposta como uma funcionalidade da crate:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --optional`

- Adicionar uma crate local como dependência:

`cargo add --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/crate</span>

- Adicionar uma dependência de desenvolvimento ou de compilação:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>

- Adicionar uma dependência com todas as funcionalidades padrão desabilitadas:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --no-default-features`
