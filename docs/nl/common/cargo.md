---
layout: page
title: common/cargo (Nederlands)
description: "Beheer Rust projecten en hun afhankelijkheden (crates)."
content_hash: 25888b6f214a0350c7ccc1b378b1e43c68ec833e
last_modified_at: 2023-10-17
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
  - title: italiano version
    url: /it/common/cargo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo

Beheer Rust projecten en hun afhankelijkheden (crates).
Sommige subcommando's zoals `build` hebben hun eigen documentatie.
Meer informatie: <https://doc.rust-lang.org/cargo>.

- Zoek naar crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekopdracht</span>

- Installeer een crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate-naam</span>

- Geef een lijst van geïnstalleerde crates:

`cargo install --list`

- Maak een nieuwe Rust-binary (bin) of -bibliotheek (lib) in de gegeven map. (Standaard is de huidige map):

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Voeg een afhankelijkheid toe aan `Cargo.toml` in de huidge map:

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">afhankelijkheid</span>

- Bouw het Rust-project in de huidige map door gebruik te maken van het release-profiel:

`cargo build --release`

- Bouw het Rust-project in de huidige map door gebruik te maken van de nachtelijkse compiler (vereist `rustup`):

`cargo +nightly build`

- Bouw met een gegeven aantal taken. (Standaard is het aantal CPU-kernen):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal_taken</span>
