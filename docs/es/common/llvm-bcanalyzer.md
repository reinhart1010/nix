---
layout: page
title: common/llvm-bcanalyzer (español)
description: "Analizador de bitcode LLVM (`.bc`)."
content_hash: dc3fcef843545714a75a0d063fe6caeace590fd0
last_modified_at: 2024-12-28
related_topics:
  - title: English version
    url: /en/common/llvm-bcanalyzer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/llvm-bcanalyzer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/llvm-bcanalyzer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># llvm-bcanalyzer

Analizador de bitcode LLVM (`.bc`).
Más información: <https://llvm.org/docs/CommandGuide/llvm-bcanalyzer.html>.

- Imprime estadísticas sobre un archivo bitcode:

`llvm-bcanalyzer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bc</span>

- Imprime una representación SGML y estadísticas sobre un archivo bitcode:

`llvm-bcanalyzer -dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bc</span>

- Lee un archivo bitcode de `stdin` y lo analiza:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.bc</span>` | llvm-bcanalyzer`
