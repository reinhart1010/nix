---
layout: page
title: common/rustc (português (Brasil))
description: "O compilador Rust."
content_hash: 0d884b7e8c98394837d3dfb77709d41e7e06a18a
related_topics:
  - title: English version
    url: /en/common/rustc.html
    icon: bi bi-globe
---
# rustc

O compilador Rust.
Processa, compila e vincula arquivos fonte da linguagem Rust.
Mais informações: <https://doc.rust-lang.org/rustc>.

- Compila um único arquivo:

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rs</span>

- Compila com alta otimização:

`rustc -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rs</span>

- Compila com informações de depuração:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo.rs</span>

- Compila com otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Exibe otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=native --print cfg`

- Exibe lista de targets:

`rustc --print target-list`

- Compila para um target específico:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_triplo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>
