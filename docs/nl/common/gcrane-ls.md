---
layout: page
title: common/gcrane-ls (Nederlands)
description: "Toon de tags in een repository."
content_hash: e8ec9f66c0b995b4e50d317af490546188dd50d2
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/gcrane-ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcrane-ls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcrane-ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcrane ls

Toon de tags in een repository.
Complexere vorm dan `crane ls`, die het mogelijk maakt om tags, manifesten en sub-repositories te tonen.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Toon de tags:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Formatteer de reactie van de registry als JSON:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --json`

- Of door repositories te recursief te doorlopen:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Toon help:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
