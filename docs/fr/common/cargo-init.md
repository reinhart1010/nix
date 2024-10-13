---
layout: page
title: common/cargo-init (français)
description: "Crée un nouveau paquet Cargo."
content_hash: 76653c36fed25c678b812936e14eba427c421190
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/cargo-init.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo-init.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-init.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo init

Crée un nouveau paquet Cargo.
Équivalent de `cargo new`, mais où spécifier un dossier est optionnel.
Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- Initialise un projet Rust binaire dans le dossier courant :

`cargo init`

- Initailise un projet de binaire Rust dans le dossier spécifié :

`cargo init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/dossier</span>

- Initialise un projet de bibliothèque Rust dans le dossier spécifié :

`cargo init --lib`

- Initialise un dépôt de système de gestion de version dans le dossier du projet (défaut : `git`) :

`cargo init --vcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg|pijul|fossil|none</span>

- Défini le nom du paquet (défaut : nom du dossier):

`cargo init --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_du_paquet</span>
