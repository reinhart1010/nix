---
layout: page
title: common/texliveonfly (Deutsch)
description: "Lade fehlende TeX Live Packages während dem Kompilieren einer `.tex` Datei herunter."
content_hash: ce5d09841ca39bcbd1ce4c359ca64f10e7fed795
related_topics:
  - title: English version
    url: /en/common/texliveonfly.html
    icon: bi bi-globe
---
# texliveonfly

Lade fehlende TeX Live Packages während dem Kompilieren einer `.tex` Datei herunter.
Weitere Informationen: <https://ctan.org/pkg/texliveonfly>.

- Lade fehlende Packages während dem Kompilieren herunter:

`texliveonfly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Verwende einen bestimmten Compiler (standardmäßig `pdflatex`):

`texliveonfly --compiler=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">compiler</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Verwende ein bestimmtes Tex Live `bin` Verzeichnis:

`texliveonfly --texlive_bin=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/texlive_bin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>
