---
layout: page
title: common/cargo-add (português (Brasil))
description: "Adiciona dependências ao arquivo `Cargo.toml` de um projeto Rust."
content_hash: 980174fe28c1deb2b3aa9e212b7fa6c27c48695c
last_modified_at: 2023-12-28
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

- Adiciona a versão mais recente de uma dependência ao projeto atual:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>

- Adiciona uma versão específica de uma dependência:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versão</span>

- Adiciona uma dependência e habilita uma ou mais funcionalidades específicas:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">funcionalidade_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">funcionalidade_2</span>

- Adiciona uma dependência opcional, que será exposta como uma funcionalidade da crate:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --optional`

- Adiciona uma crate local como dependência:

`cargo add --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/crate</span>

- Adiciona uma dependência de desenvolvimento ou de compilação:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>

- Adiciona uma dependência com todas as funcionalidades padrão desabilitadas:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependência</span>` --no-default-features`
