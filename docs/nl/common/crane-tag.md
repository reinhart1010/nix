---
layout: page
title: common/crane-tag (Nederlands)
description: "Efficiënt taggen van een remote image zonder het te downloaden, wat verschilt van het `copy` commando."
content_hash: 56c55e230392ef1a4eba7faf89c39e1a1c520340
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/crane-tag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane tag

Efficiënt taggen van een remote image zonder het te downloaden, wat verschilt van het `copy` commando.
Het slaat de controles van laagbestaan over omdat we weten dat de manifest al bestaat, wat het iets sneller maakt.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- Tag een remote image:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Toon de help:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
