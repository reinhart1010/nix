---
layout: page
title: common/crane-rebase (Nederlands)
description: "Rebase een image op een nieuw basisimage."
content_hash: d70521978507214877cf5b7fade90ba83c87305d
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-rebase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-rebase.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-rebase.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane rebase

Rebase een image op een nieuw basisimage.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- Rebase image:

`crane rebase`

- Nieuwe basisimage om in te voegen:

`crane rebase --new_base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>

- Oude basisimage om te verwijderen:

`crane rebase --old_base `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>

- Tag om toe te passen op de gerebaseerde image:

`crane rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Toon help:

`crane rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
