---
layout: page
title: common/gcrane-gc (Nederlands)
description: "Toon images die niet getagged zijn."
content_hash: a74dece0e71c7516276b974691909145bb1d66f2
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/gcrane-gc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcrane-gc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gcrane-gc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcrane gc

Toon images die niet getagged zijn.
Zal berekenen welke images opgeruimd kunnen worden met garbage-collection.
Dit kan uitgevoerd worden met `gcrane delete` om ze daadwerkelijk op te ruimen.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Toon niet getagde images:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Recursief door de repositories heen:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Toon help:

`gcrane gc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
