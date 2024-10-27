---
layout: page
title: common/crane-flatten (Nederlands)
description: "Flatten de lagen van een image tot een enkele laag."
content_hash: b2c67041bdc53f3d9a6823a26dae2b4dcc7567c9
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/crane-flatten.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-flatten.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane flatten

Flatten de lagen van een image tot een enkele laag.
Push de digest naar de oorspronkelijke image-repository als er geen tags zijn opgegeven.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Flatten een image:

`crane flatten`

- Pas een nieuwe tag toe op de geflatteerde image:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Toon help:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
