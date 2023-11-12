---
layout: page
title: common/pdftex (Deutsch)
description: "Kompiliere eine TeX Quelldatei in ein PDF Dokument."
content_hash: 19facff7c797d75f5249549a0aed0ad5d8852ed7
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pdftex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdftex

Kompiliere eine TeX Quelldatei in ein PDF Dokument.
Weitere Informationen: <https://www.tug.org/applications/pdftex/>.

- Kompiliere ein PDF Dokument:

`pdftex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein PDF Dokument und gib ein bestimmtes Output-Verzeichnis an:

`pdftex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein PDF Dokument und stoppe bei jedem Fehler:

`pdftex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>
