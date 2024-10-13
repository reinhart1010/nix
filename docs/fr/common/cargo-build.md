---
layout: page
title: common/cargo-build (français)
description: "Compile un paquet local et toutes ses dépendances."
content_hash: 1f109a11c0b863ee1a5d6a34832a7f0acdd7fc62
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/cargo-build.html
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-build.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo build

Compile un paquet local et toutes ses dépendances.
Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- Compile un ou plusieurs paquets définis dans le manifeste `Cargo.toml` dans le dossier local :

`cargo build`

- Compile les artefacts avec le mode publication, avec des optimisations :

`cargo build --release`

- Le fichier `Cargo.lock` doit être à jour :

`cargo build --locked`

- Compile tous les paquets de l'espace de travail :

`cargo build --workspace`

- Compile un paquet spécifique :

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquet</span>

- Compile uniquement le binaire spécifié :

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_binaire</span>

- Compile uniquement le test cible spécifié :

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_test</span>
