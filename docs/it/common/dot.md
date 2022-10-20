---
layout: page
title: common/dot (italiano)
description: "Strumento da linea di comando per produrre disegni a livelli di grafi orientati."
content_hash: 1edd6f3a28da7c64e53675034709df10b4a5928a
related_topics:
  - title: English version
    url: /en/common/dot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dot.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dot

Strumento da linea di comando per produrre disegni a livelli di grafi orientati.
Maggiori informazioni: <https://graphviz.org/doc/info/command.html>.

- Renderizza un'immagine determinando il nome del file di output dal nome del file di input ed il formato:

`dot -Tpng -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.dot</span>

- Crea una SVG da un file DOT:

`dot -Tsvg -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_output.svg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.dot</span>
