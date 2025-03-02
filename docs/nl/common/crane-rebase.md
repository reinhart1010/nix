---
layout: page
title: common/crane-rebase (Nederlands)
description: "Rebase een image op een nieuw basisimage."
content_hash: 5d8525fc2895776c9933e19f9dd4c6c875dd3ca3
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/crane-rebase.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-rebase.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane rebase

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

- Toon de help:

`crane rebase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
