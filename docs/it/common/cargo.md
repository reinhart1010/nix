---
layout: page
title: common/cargo (italiano)
description: "Gestore di pacchetti di Rust."
content_hash: bbf17b89eb257c8bdef5d43216d8909b4266bab6
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
---
# cargo

Gestore di pacchetti di Rust.
Gestisce progetti Rust ed i moduli dai quali sono dipendenti (detti crate).
Alcuni comandi aggiuntivi, come `cargo build`, hanno la propria documentazione.
Maggiori informazioni: <https://crates.io/>.

- Cerca una crate:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termine_di_ricerca</span>

- Installa una crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_crate</span>

- Elenca crate installate:

`cargo install --list`

- Crea un nuovo progetto Rust binario o di libreria nella directory corrente:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Crea un nuovo progetto Rust binario o di libreria nella directory specificata:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/a/directory</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Builda il progetto Rust nella cartella corrente:

`cargo build`

- Builda utilizzando più job (thread) paralleli:

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_job</span>
