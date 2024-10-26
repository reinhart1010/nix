---
layout: page
title: common/crane-ls (Nederlands)
description: "Toon de tags in een repository."
content_hash: 2c1e03e013888aa72b645974c4713d26f4935444
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-ls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane ls

Toon de tags in een repository.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_ls.md>.

- Toon de tags:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>

- Print de volledige image-referentie:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository</span>` --full-ref`

- Sla digest-tags over:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--omit-digest-tags</span>

- Toon help:

`crane ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
