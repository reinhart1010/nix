---
layout: page
title: common/rustc (português (Brasil))
description: "O compilador Rust."
content_hash: 49e89bcf8a48e247d05259c63504cf14ece16370
last_modified_at: 2024-01-07
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
Projetos Rust geralmente usam o `cargo` em vez de chamar `rustc` diretamente.
Mais informações: <https://doc.rust-lang.org/rustc>.

- Compila uma crate binária:

`rustc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Compila com otimizações (s significa otimizar o tamanho do binário; z é o mesmo com ainda mais otimizações):

`rustc -C lto -C opt-level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3|s|z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Compila com informações de depuração:

`rustc -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Explica uma mensagem de erro:

`rustc --explain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">código_de_erro</span>

- Compila com otimizações específicas de arquitetura para a CPU atual:

`rustc -C target-cpu=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">native</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>

- Exibe lista de targets:

`rustc --print target-list`

- Compila para um target específico:

`rustc --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_triplo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.rs</span>
