---
layout: page
title: common/cargo (français)
description: "Gestion d'un projet Rust et ses dependences (crates)."
content_hash: bea5294a8f35aab51f42e6fbe43aa47a56ea1490
last_modified_at: 2024-10-05
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
  - title: 中文 version
    url: /zh/common/cargo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo

Gestion d'un projet Rust et ses dependences (crates).
Certaines sous-commandes comme `build` ont leurs propres documentations.
Plus d'informations : <https://doc.rust-lang.org/cargo>.

- Rechercher des crates :

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recherche</span>

- Installer un crate :

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_crate</span>

- Lister les crates déjà installés :

`cargo install --list`

- Crée un nouveau binaire ou librairie du projet Rust dans les dossiers spécifiés (ou dans le dossier courant par défaut) :

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Compile le projet Rust dans le dossier courant en utilisant le profil release :

`cargo build --release`

- Compiler le projet Rust dans le dossier courant en utilisant le compilateur nightly :

`cargo +nightly build`

- Compiler en utilisant un nombre spécifique de threads (par défaut on prend le nombre de coeurs du CPU) :

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_threads</span>
