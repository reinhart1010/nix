---
layout: page
title: common/pdflatex (Deutsch)
description: "Kompiliere eine LaTeX Quelldatei in ein PDF Dokument."
content_hash: 6fc06c27fd68a26992648cb2b5c28d9daeb608a4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pdflatex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdflatex

Kompiliere eine LaTeX Quelldatei in ein PDF Dokument.
Weitere Informationen: <https://manned.org/pdflatex>.

- Kompiliere ein PDF Dokument:

`pdflatex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein PDF Dokument und gib ein bestimmtes Output-Verzeichnis an:

`pdflatex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein PDF Dokument und stoppe bei jedem Fehler:

`pdflatex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>
