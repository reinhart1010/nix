---
layout: page
title: common/cargo (Deutsch)
description: "Verwalte Rust-Projekte und deren Abhängigkeiten (crates)."
content_hash: f56f4f718a903d1effd7c4cf786309e6c32ff140
related_topics:
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

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo

Verwalte Rust-Projekte und deren Abhängigkeiten (crates).
Manche Unterbefehle wie `cargo build` sind separat dokumentiert.
Weitere Informationen: <https://crates.io>.

- Suche nach Abhängigkeiten (crates):

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suche</span>

- Installiere eine Abhängigkeit (crate):

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">abhängigkeit</span>

- Liste alle installierten Abhängigkeiten (crates) auf:

`cargo install --list`

- Erzeuge ein neues Rust-Projekt als Anwendung oder Bibliothek im aktuellen Verzeichnis:

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Erzeuge ein neues Rust-Projekt als Anwendung oder Bibliothek im angegebenen Verzeichnis:

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Erstelle (bzw. kompiliere) ein Rust-Projekt im aktuellen Verzeichnis:

`cargo build`

- Erstelle (bzw. kompiliere) ein Rust-Projekt mit einer bestimmten Anzahl an Threads (standardmäßig die Anzahl der CPU-Kerne):

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">thread_anzahl</span>
