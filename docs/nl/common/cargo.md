---
layout: page
title: common/cargo (Nederlands)
description: "Rust pakketbeheerder."
content_hash: 8ab2a344551abad3ccbbfa3d840d5f1af0c3f72d
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

Rust pakketbeheerder.
Beheer Rust projecten en hun afhankelijkheden (crates).
Meer informatie: <https://crates.io>.

- Zoek naar crates:

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekopdracht</span>

- Installeer een crate:

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">crate-naam</span>

- Geef een lijst van geïnstalleerde crates:

`cargo install --list`

- Maak een nieuwe Rust-binary (bin) of -bibliotheek (lib) in de huidige map:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Maak een nieuwe Rust-binary (bin) of -bibliotheek (lib) in de gegeven map:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Bouw het Rust-project in de huidige map:

`cargo build`

- Bouw met een gegeven aantal taken. (Standaard is het aantal CPU-kernen):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal_taken</span>
