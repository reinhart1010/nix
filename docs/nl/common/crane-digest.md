---
layout: page
title: common/crane-digest (Nederlands)
description: "Verkrijg de digest van een image."
content_hash: 634c240de93bee72ce7755dcc9983369b303bc52
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/crane-digest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-digest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane digest

Verkrijg de digest van een image.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Verkrijg de digest van een image:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>

- Print de volledige image-referentie op basis van de digest:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` --full-ref`

- Specificeer het pad naar de tarball met de image:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` --tarball `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>

- Toon de help:

`crane digest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
