---
layout: page
title: common/cargo-build (español)
description: "Compila un paquete local y todas sus dependencias."
content_hash: 64f47b5e780293191aeec34db79ebf61f770adc5
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/cargo-build.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cargo-build.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-build.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-build.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo build

Compila un paquete local y todas sus dependencias.
Más información: <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Construye el paquete o los paquetes definidos por el archivo manifiesto `Cargo.toml` en la ruta local:

`cargo build`

- Construye artefactos en modo de lanzamiento, con optimizaciones:

`cargo build --release`

- Exige que `Cargo.lock` esté actualizado:

`cargo build --locked`

- Construye todos los paquetes en el espacio de trabajo:

`cargo build --workspace`

- Construye un paquete en específico:

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Construye solo el binario especificado:

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Construye solamente el objetivo de prueba especificado:

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_prueba</span>
