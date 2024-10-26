---
layout: page
title: common/crane-tag (Nederlands)
description: "Efficiënt taggen van een remote image zonder het te downloaden, wat verschilt van het `copy` commando."
content_hash: 6ed345935e2a9c51c6236d8ca514fd86d0047aad
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-tag.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-tag.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-tag.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane tag

Efficiënt taggen van een remote image zonder het te downloaden, wat verschilt van het `copy` commando.
Het slaat de controles van laagbestaan over omdat we weten dat de manifest al bestaat, wat het iets sneller maakt.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_tag.md>.

- Tag een remote image:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Toon help:

`crane tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
