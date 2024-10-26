---
layout: page
title: common/crane-append (Nederlands)
description: "Push een image gebaseerd op een (optionele) basisimage."
content_hash: 8faf9d3d639a457ad4db84e982302a027484d628
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-append.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-append.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-append.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane append

Push een image gebaseerd op een (optionele) basisimage.
Voegt lagen toe met de inhoud van de opgegeven tarballs.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>.

- Push een image gebaseerd op een basisimage:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-b|--base</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>

- Push een image met een toegevoegde laag vanuit een tarball:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--new_layer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">layer_naam1 layer_naam2 ...</span>

- Push een image met een toegevoegde laag met een nieuwe tag:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--new_tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Push de resulterende image naar een nieuwe tarball:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>

- Gebruik een lege basisimage van het type OCI-media in plaats van Docker:

`crane append --oci-empty-base`

- Annoteer de resulterende image als gebaseerd op de basisimage:

`crane append --set-base-image-annotations`

- Toon help:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
