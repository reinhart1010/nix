---
layout: page
title: common/tex (Deutsch)
description: "Kompiliere eine TeX Quelldatei in ein DVI Dokument."
content_hash: f198ebc28d5177517f3869dafa48647c4546f4f0
related_topics:
  - title: English version
    url: /en/common/tex.html
    icon: bi bi-globe
---
# tex

Kompiliere eine TeX Quelldatei in ein DVI Dokument.
Weitere Informationen: <https://www.tug.org/begin.html>.

- Kompiliere ein DVI Dokument:

`tex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein DVI Dokument und gib ein bestimmtes Output-Verzeichnis an:

`tex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>

- Kompiliere ein DVI Dokument und stoppe bei jedem Fehler:

`tex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quelldatei.tex</span>
