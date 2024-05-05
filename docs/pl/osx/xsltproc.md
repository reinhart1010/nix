---
layout: page
title: osx/xsltproc (polski)
description: "Przekształcanie XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML)."
content_hash: 83eb859bab1f8483a46677b98d74d627d8378e66
last_modified_at: 2024-05-05
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/xsltproc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xsltproc

Przekształcanie XML z XSLT w celu uzyskania wyjścia (zwykle HTML lub XML).
Więcej informacji: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- Przekształcenie pliku XML za pomocą określonego arkusza stylów XSLT:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/arkusza_stylow.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku.xml</span>

- Przekaż wartość do parametru w arkuszu stylów:

`xsltproc --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku_wyjscia.html</span>` --stringparam "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wartosc</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/arkusza_stylow.xslt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sciezka/do/pliku.xml</span>
