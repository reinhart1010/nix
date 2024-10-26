---
layout: page
title: common/crane-version (Nederlands)
description: "Print de versie van een binary."
content_hash: e297e3cdcdd961b1f708f97c903e153fb2a66556
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-version.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-version.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-version.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane version

Print de versie van een binary.
De versiestring is volledig afhankelijk van hoe de binary is gebouwd, dus je moet niet afhankelijk zijn van het versieformaat. Het kan zonder voorafgaande kennisgeving veranderen.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_version.md>.

- Toon versie:

`crane version`

- Toon help:

`crane version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
