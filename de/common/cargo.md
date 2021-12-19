---
layout: page
title: common/cargo (Deutsch)
description: "Verwalte Rust-Projekte und deren Abhängigkeiten (crates)."
content_hash: bbc6aaf9acf4d48f8f86bffe24dedcd2e25c8cf5
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
---
# cargo

Verwalte Rust-Projekte und deren Abhängigkeiten (crates).
Manche Unterbefehle wie `cargo build` sind separat dokumentiert.
Weitere Informationen: <https://crates.io/>.

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
