---
layout: page
title: common/cargo-doc (português (Brasil))
description: "Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline."
content_hash: ecc827c08421289ab4fe6c748c95069ae53b4c70
last_modified_at: 2023-08-05
related_topics:
  - title: English version
    url: /en/common/cargo-doc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-doc.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo doc

Constrói e visualiza a documentação de um pacote Rust, opcionalmente em modo offline.
Mais informações: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Construir a documentação padrão do pacote e mostrá-la no navegador:

`cargo doc --open`

- Construir a documentação sem acessar a rede:

`cargo doc --offline`

- Visualizar a documentação de um pacote específico:

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Visualizar a documentação de um pacote específico sem acessar a rede:

`cargo doc --open --offline --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>
