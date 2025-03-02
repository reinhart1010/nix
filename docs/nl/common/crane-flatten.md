---
layout: page
title: common/crane-flatten (Nederlands)
description: "Flatten de lagen van een image tot een enkele laag."
content_hash: 73bf5fccf664b5d037d859f018a1fceaed0f4a5f
last_modified_at: 2025-03-02
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

- Toon de help:

`crane flatten `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
