---
layout: page
title: common/llvm-cat (español)
description: "Concatena archivos bitcode LLVM (`.bc`)."
content_hash: e9b6fb45d71b5ff84ba604cce62a580d65220d71
last_modified_at: 2024-12-28
related_topics:
  - title: English version
    url: /en/common/llvm-cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llvm-cat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llvm-cat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llvm-cat

Concatena archivos bitcode LLVM (`.bc`).
Más información: <https://github.com/llvm/llvm-project/blob/main/llvm/tools/llvm-cat/llvm-cat.cpp>.

- Concatena archivos de bitcode:

`llvm-cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1.bc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2.bc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/concatenado.bc</span>
