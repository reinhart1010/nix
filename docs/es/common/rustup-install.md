---
layout: page
title: common/rustup-install (español)
description: "Install or update Rust toolchains."
content_hash: 83e13f7985abd51d58f4beec183d408942aef013
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/rustup-install.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rustup-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rustup-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rustup install

Install or update Rust toolchains.
Este comando es un alias de `rustup update`, pero sólo puede instalar/actualizar una cadena de herramientas (toolchain) a la vez.
Más información: <https://rust-lang.github.io/rustup>.

- Instalar o actualizar una cadena de herramientas específica (para más información, vea `rustup help toolchain`):

`rustup install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">toolchain</span>
