---
layout: page
title: osx/head (Nederlands)
description: "Geef het eerste deel van bestanden weer."
content_hash: 032fa91214f9a4ac6d1d7d93cc6b9ab31c726e0d
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/osx/head.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/head.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/head.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># head

Geef het eerste deel van bestanden weer.
Meer informatie: <https://keith.github.io/xcode-man-pages/head.1.html>.

- Geef de eerste paar regels van een bestand weer:

`head --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef de eerste paar bytes van een bestand weer:

`head --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef alles behalve de laatste paar regels van een bestand weer:

`head --lines -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef alles behalve de laatste paar bytes van een bestand weer:

`head --bytes -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
