---
layout: page
title: common/m4b-tool (español)
description: "Fusiona, divide y manipula archivos de audiolibros con capítulos."
content_hash: 7e75c531b7354861267c596c7fe228c6559eba16
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/common/m4b-tool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/m4b-tool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># m4b-tool

Fusiona, divide y manipula archivos de audiolibros con capítulos.
Más información: <https://github.com/sandreas/m4b-tool>.

- Crea un audiolibro con los archivos de audio del directorio de entrada:

`m4b-tool merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_de_entrada</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/fusionado.m4b</span>

- Hace capítulos utilizando los nombres de los archivos de entrada:

`m4b-tool merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio_de_entrada</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/fusionado.m4b</span>` --use-filenames-as-chapters`
