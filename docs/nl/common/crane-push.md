---
layout: page
title: common/crane-push (Nederlands)
description: "Stuur lokale image-inhoud naar een externe registry."
content_hash: 2dba5df657a3a45c9ffdf4d487da87e2f8378cf4
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-push.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-push.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-push.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane push

Stuur lokale image-inhoud naar een externe registry.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

- Stuur lokale image naar externe registry:

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>

- Pad naar bestand met lijst van gepubliceerde image-referenties:

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` --image-refs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/filenaam</span>

- Stuur een verzameling images als een enkele index (vereist als pad meerdere images heeft):

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` --index`

- Toon help:

`crane push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
