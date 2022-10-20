---
layout: page
title: common/cargo (español)
description: "Gestiona proyectos Rust y sus dependencias de módulos (crates)."
content_hash: 1373612c7d527e6fab77ecade3e7d335a9149778
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
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
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo

Gestiona proyectos Rust y sus dependencias de módulos (crates).
Algunos subcomandos como `cargo build` tienen su propia documentación de uso.
Más información: <https://crates.io>.

- Busca crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_de_búsqueda</span>

- Instala un crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_módulo</span>

- Lista crates instalados:

`cargo install --list`

- Crea un nuevo proyecto Rust binario o biblioteca en el directorio actual:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Crea un nuevo proyecto Rust binario o biblioteca en el directorio especificado:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Compila el proyecto Rust en el directorio actual:

`cargo build`

- Compila el proyecto Rust en el directorio actual usando el compilador nightly:

`cargo +nightly build`

- Compila el proyecto Rust en el directorio actual usando un número específico de hilos (por defecto es el número de núcleos de la CPU):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_de_hilos</span>
