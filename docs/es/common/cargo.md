---
layout: page
title: common/cargo (español)
description: "Gestiona proyectos Rust y sus dependencias de módulos (crates)."
content_hash: 72cf27e9ea042a8995fe3ee0266ff1788c28d9ec
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cargo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cargo.html
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
tldri18n_status: 2
---
# cargo

Gestiona proyectos Rust y sus dependencias de módulos (crates).
Algunos subcomandos como `build` tienen su propia documentación de uso.
Más información: <https://doc.rust-lang.org/cargo>.

- Busca crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cadena_de_busqueda</span>

- Instala un crate binario:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_crate</span>

- Lista los crates binarios instalados:

`cargo install --list`

- Crea un nuevo proyecto Rust binario o de biblioteca en el directorio especificado (o en el directorio de trabajo actual por defecto):

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Añade una dependencia a `Cargo.toml` en el directorio actual:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dependencia</span>

- Construye el proyecto Rust en el directorio actual utilizando el perfil de lanzamiento:

`cargo build --release`

- Construye el proyecto Rust en el directorio actual utilizando el compilador nightly (requiere `rustup`):

`cargo +nightly build`

- Construye usando un número específico de hilos (por defecto es el número de CPUs lógicas):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_hilos</span>
