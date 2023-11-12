---
layout: page
title: common/rustc (português (Brasil))
description: "O compilador Rust."
content_hash: 10a72c0397d8e5febacf12bb2e82353a29d16f61
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/rustc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rustc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rustc

O compilador Rust.
Processa, compila e vincula arquivos fonte da linguagem Rust.
Mais informações: <https://doc.rust-lang.org/rustc>.

- Compila um único arquivo:

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Compila com alta otimização:

`rustc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Compila com informações de depuração:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Compila com otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Exibe otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native --print cfg`

- Exibe lista de targets:

`rustc --print target-list`

- Compila para um target específico:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_triplo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>
