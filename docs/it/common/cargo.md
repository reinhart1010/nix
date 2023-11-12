---
layout: page
title: common/cargo (italiano)
description: "Gestore di pacchetti di Rust."
content_hash: 03d477c7148495444c0ce6de4c7f7240734bd76a
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cargo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cargo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo

Gestore di pacchetti di Rust.
Gestisce progetti Rust ed i moduli dai quali sono dipendenti (detti crate).
Alcuni comandi aggiuntivi, come `cargo build`, hanno la propria documentazione.
Maggiori informazioni: <https://doc.rust-lang.org/cargo>.

- Cerca una crate:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termine_di_ricerca</span>

- Installa una crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_crate</span>

- Elenca crate installate:

`cargo install --list`

- Crea un nuovo progetto Rust binario o di libreria nella directory corrente:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Crea un nuovo progetto Rust binario o di libreria nella directory specificata:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Builda il progetto Rust nella directory corrente:

`cargo build`

- Builda utilizzando più job (thread) paralleli:

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_job</span>
