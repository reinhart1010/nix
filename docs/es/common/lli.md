---
layout: page
title: common/lli (español)
description: "Ejecuta directamente programas desde el código de bits LLVM (bitcode)."
content_hash: ed1e566f862276a60c85bd8f60bd90185687c029
last_modified_at: 2024-12-29
related_topics:
  - title: English version
    url: /en/common/lli.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/lli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lli

Ejecuta directamente programas desde el código de bits LLVM (bitcode).
Más información: <https://www.llvm.org/docs/CommandGuide/lli.html>.

- Ejecuta un código de bits o un archivo IR:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ll</span>

- Ejecuta con argumentos de línea de comandos:

`lli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">primer_argumento segundo_argumento ...</span>

- Habilita todas las optimizaciones:

`lli -O3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ll</span>

- Carga una biblioteca dinámica antes de vincular:

`lli --dlopen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/biblioteca.dll</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.ll</span>
