---
layout: page
title: common/gcrane-ls (Nederlands)
description: "Toon de tags in een repository."
content_hash: 95edbda6abd2d7466673972508d017fde7b88f0d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/gcrane-ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcrane-ls.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane ls

Toon de tags in een repository.
Complexere vorm dan `crane ls`, die het mogelijk maakt om tags, manifesten en sub-repositories te tonen.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Toon de tags:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Formatteer de reactie van de registry als JSON:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --json`

- Of door repositories te recursief te doorlopen:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Toon de help:

`gcrane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
