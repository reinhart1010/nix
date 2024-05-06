---
layout: page
title: osx/xsltproc (polski)
description: "Przekształcanie XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML)."
content_hash: 83eb859bab1f8483a46677b98d74d627d8378e66
last_modified_at: 2024-05-06
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

Przekształcanie XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML).
Więcej informacji: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- Przekształcenie pliku XML za pomocą określonego arkusza stylów XSLT:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/arkusza_stylow.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku.xml</span>

- Przekaż wartość do parametru w arkuszu stylów:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.html</span>` --stringparam "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wartosc</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/arkusza_stylow.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku.xml</span>
