---
layout: page
title: common/cargo-bench (français)
description: "Compile et exécute des benchmarks."
content_hash: c634a887a555b7329af991ef966ae5f79ceaeb9c
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/cargo-bench.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo-bench.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cargo-bench.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-bench.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo bench

Compile et exécute des benchmarks.
Plus d'informations : <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>.

- Exécute tous les benchmarks d'un paquet :

`cargo bench`

- Ne pas arréter quand un benchmark échoue :

`cargo bench --no-fail-fast`

- Compile, mais n'exécute pas les benchmarks :

`cargo bench --no-run`

- Exécute le benchmark spécifié :

`cargo bench --bench `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benchmark</span>

- Exécute les benchmarks avec un profile spécifique (défaut : `bench`) :

`cargo bench --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile</span>

- Exécute les benchmarks sur tous les exemples cibles :

`cargo bench --examples`

- Exécute les benchmarks sur tous les binaires cibles :

`cargo bench --bins`

- Exécute les benchmarks sur la bibliothèque du paquet :

`cargo bench --lib`
