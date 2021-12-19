---
layout: page
title: common/latex (Deutsch)
description: "Kompiliere eine LaTeX Quelldatei in ein DVI Dokument."
content_hash: 4036165e86948006c1f8201deba17f4e3760d42c
related_topics:
  - title: English version
    url: /en/common/latex.html
    icon: bi bi-globe
---
# latex

Kompiliere eine LaTeX Quelldatei in ein DVI Dokument.
Weitere Informationen: <https://www.latex-project.org>.

- Kompiliere ein DVI Dokument:

`latex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein DVI Dokument und gib ein bestimmtes Output-Verzeichnis an:

`latex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein DVI Dokument und stoppe bei jedem Fehler:

`latex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>
