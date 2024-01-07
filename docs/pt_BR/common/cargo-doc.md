---
layout: page
title: common/cargo-doc (português (Brasil))
description: "Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline."
content_hash: 02892ce3005582ae6f1c2494bdabab72c7ee2b5c
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/common/cargo-doc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo doc

Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline.
Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Constrói a documentação do projeto atual e de todas as dependências:

`cargo doc`

- Não constrói documentação de dependências:

`cargo doc --no-deps`

- Constrói e visualiza a documentação em um navegador:

`cargo doc --open`

- Constrói e visualiza a documentação de um pacote específico:

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>
