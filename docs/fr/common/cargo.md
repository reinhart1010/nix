---
layout: page
title: common/cargo (français)
description: "Gestion d'un projet Rust et ses dependences (crates)."
content_hash: 981f7869aa74b8ba23f3686ccce3e7782f1eaf5d
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo

Gestion d'un projet Rust et ses dependences (crates).
Certaines sous-commandes comme `cargo build` ont leurs propres documentations.
Plus d'informations : <https://crates.io/>.

- Rechercher des crates :

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recherche</span>

- Installer un crate :

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_crate</span>

- Lister les crates déjà installés :

`cargo install --list`

- Créer un nouveau binaire ou librairie du projet Rust dans le dossier courant :

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Créer un nouveau binaire ou librairie du projet Rust dans un dossier spécifique :

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>

- Compiler le projet Rust dans le dossier courant :

`cargo build`

- Compiler le projet Rust dans le dossier courant en utilisant le compilateur nightly :

`cargo +nightly build`

- Compiler en utilisant un nombre spécifique de threads (par défaut on prend le nombre de coeurs du CPU) :

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_threads</span>
