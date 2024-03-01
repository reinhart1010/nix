---
layout: page
title: common/deno (français)
description: "Un environnement d’exécution sécurisé pour JavaScript et TypeScript."
content_hash: c0f81a69f7ca24ab9c180c6c4f16d1b66e2c787e
last_modified_at: 2024-03-01
related_topics:
  - title: Deutsch version
    url: /de/common/deno.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/deno.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/deno.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/deno.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/deno.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/deno.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/deno.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># deno

Un environnement d’exécution sécurisé pour JavaScript et TypeScript.
Plus d'information : <https://deno.land>.

- Exécute un fichier JavaScript ou TypeScript :

`deno run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/fichier.ts</span>

- Démarre un REPL (shell interactif) :

`deno`

- Exécute un fichier avec l'accès au réseau activé :

`deno run --allow-net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/du/fichier.ts</span>

- Exécute un fichier à partir d’une URL :

`deno run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://deno.land/std/examples/welcome.ts</span>

- Installe un script exécutable à partir d’une URL :

`deno install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://deno.land/std/examples/colors.ts</span>
