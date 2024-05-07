---
layout: page
title: osx/xsltproc (polski)
description: "Przekształć XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML)."
content_hash: 02421e684f01fabddae9e9b580c1bb64b8816085
last_modified_at: 2024-05-07
related_topics:
  - title: English version
    url: /en/osx/xsltproc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/xsltproc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xsltproc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xsltproc

Przekształć XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML).
Więcej informacji: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- Przekształć plik XML za pomocą określonego arkusza stylów XSLT:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjścia.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/arkusza_stylów.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.xml</span>

- Przekaż wartość do parametru w arkuszu stylów:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku_wyjścia.html</span>` --stringparam "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wartość</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/arkusza_stylów.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.xml</span>
