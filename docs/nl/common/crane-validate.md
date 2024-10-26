---
layout: page
title: common/crane-validate (Nederlands)
description: "Valideer of een image goed is gevormd."
content_hash: 1f5755277729d6c679b316a4b06a4fa16d1eff51
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-validate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-validate.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-validate.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane validate

Valideer of een image goed is gevormd.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- Valideer een image:

`crane validate`

- Sla het downloaden/digiteren van lagen over:

`crane validate --fast`

- Naam van de remote image om te valideren:

`crane validate --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>

- Pad naar tarball om te valideren:

`crane validate --tarball `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>

- Toon help:

`crane validate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
