---
layout: page
title: common/crane-append (Nederlands)
description: "Push een image gebaseerd op een (optionele) basisimage."
content_hash: 2ce062c5142d0f35ef3544f1fc50a1a6c0a845c8
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/crane-append.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-append.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane append

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

- Toon de help:

`crane append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
