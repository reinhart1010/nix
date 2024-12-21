---
layout: page
title: common/elinks (español)
description: "Un navegador basado en texto similar a `lynx`."
content_hash: 073d3e48171816cd1a461017dee1244c596ff690
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/common/elinks.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/elinks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/elinks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/elinks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># elinks

Un navegador basado en texto similar a `lynx`.
Más información: <https://github.com/rkd77/elinks>.

- Inicia ELinks:

`elinks`

- Sale de ELinks:

`<Ctrl> + C`

- Vuelca la página web a la consola, colorea el texto con códigos de control ANSI:

`elinks -dump -dump-color-mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
