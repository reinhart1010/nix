---
layout: page
title: common/fzf (español)
description: "Buscador aproximado (fuzzy search) de la línea de comando."
content_hash: 09858217322c09cddbecd484fa6e345e5e34f683
last_modified_at: 2024-12-01
related_topics:
  - title: English version
    url: /en/common/fzf.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fzf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fzf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/fzf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/fzf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fzf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fzf

Buscador aproximado (fuzzy search) de la línea de comando.
Parecido a `sk`.
Más información: <https://github.com/junegunn/fzf>.

- Aplica `fzf` a todos los archivos en el directorio especificado:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` -type f | fzf`

- Aplica `fzf` a los procesos en ejecución:

`ps aux | fzf`

- Selecciona varios archivos con `Shift + Tab` y los escribe a un archivo:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>` -type f | fzf --multi > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Aplica `fzf` con una consulta especificada:

`fzf --query "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">consulta</span>`"`

- Aplica `fzf` en las entradas que comienzan con `programa` y finalizan con `go`, `rb`, o `py`:

`fzf --query "^programa go$ | rb$ | py$"`

- Aplica `fzf` en entradas que no coinciden con `pyc` y coinciden exactamente con `travis`:

`fzf --query "!pyc 'travis"`
