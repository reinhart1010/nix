---
layout: page
title: common/crane-pull (Nederlands)
description: "Haal externe images op via referentie en sla hun inhoud lokaal op."
content_hash: 6feeb26f730a2bb651fd74747beb410c229e2db7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/crane-pull.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-pull.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane pull

Haal externe images op via referentie en sla hun inhoud lokaal op.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

- Haal externe image op:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>

- Bewaar de image-referentie die is gebruikt om op te halen als een annotatie wanneer gebruikt met --format=oci:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>` --annotate-ref`

- Pad naar cache-image-lagen:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--cache_path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/cache</span>

- Formaat waarin images moeten worden opgeslagen (standaard 'tarball'):

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format_naam</span>

- Toon de help:

`crane pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
