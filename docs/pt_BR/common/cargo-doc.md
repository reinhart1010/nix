---
layout: page
title: common/cargo-doc (português (Brasil))
description: "Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline."
content_hash: 79c006a3cbdb41a13b84d0ae55901cbc004c642c
last_modified_at: 2023-12-28
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

- Constrói a documentação padrão do pacote e mostrá-la no navegador:

`cargo doc --open`

- Constrói a documentação sem acessar a rede:

`cargo doc --offline`

- Visualiza a documentação de um pacote específico:

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Visualiza a documentação de um pacote específico sem acessar a rede:

`cargo doc --open --offline --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>
