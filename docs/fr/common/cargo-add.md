---
layout: page
title: common/cargo-add (français)
description: "Ajoute des dépendences au manifeste `Cargo.toml` d'un projet Rust."
content_hash: eb8cde93736badfdd9bd893ecea1ca941ef4f7aa
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/cargo-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-add.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-add.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-add.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo add

Ajoute des dépendences au manifeste `Cargo.toml` d'un projet Rust.
Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- Ajoute la dernière version d'une dépendance au projet courant :

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépendance</span>

- Ajoute une version spécifique d'une dépendance :

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépendance</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Ajoute une dépendance et active une ou plusieures fonctionnalités :

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépendance</span>` --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fonctionnalité_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fonctionnalité_2</span>

- Ajoute une dépendance optionnelle, qui sera exposée comme une fonctionnalité du crate :

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépendance</span>` --optional`

- Ajoute un crate local en tant que dépendance :

`cargo add --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/crate</span>

- Ajoute une dépendance de développement ou de compilation :

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépendance</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>

- Ajoute une dépendance avec toutes les fonctionnalités par défaut désactivées :

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépendance</span>` --no-default-features`
