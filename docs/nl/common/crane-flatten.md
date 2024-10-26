---
layout: page
title: common/crane-flatten (Nederlands)
description: "Flatten de lagen van een image tot een enkele laag."
content_hash: b2c67041bdc53f3d9a6823a26dae2b4dcc7567c9
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-flatten.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-flatten.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-flatten.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane flatten

Flatten de lagen van een image tot een enkele laag.
Push de digest naar de oorspronkelijke image-repository als er geen tags zijn opgegeven.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Flatten een image:

`crane flatten`

- Pas een nieuwe tag toe op de geflatteerde image:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Toon help:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
