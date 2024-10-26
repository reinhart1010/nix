---
layout: page
title: common/crane-catalog (Nederlands)
description: "Toon de repositories in een registry."
content_hash: 9573c6f909968535cdda9b9798668da1f70be3ad
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-catalog.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-catalog.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-catalog.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane catalog

Toon de repositories in een registry.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_catalog.md>.

- Toon de repositories in een registry:

`crane catalog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_adres</span>

- Print de volledige image-referentie:

`crane catalog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry_adres</span>` --full-ref`

- Toon help:

`crane catalog `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
