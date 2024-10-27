---
layout: page
title: common/crane-export (Nederlands)
description: "Exporteer het bestandssysteem van een containerimage als een tarball."
content_hash: ece668a0428071d5cdd9d4ece6cd19a8f35030c5
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/crane-export.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-export.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane export

Exporteer het bestandssysteem van een containerimage als een tarball.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Schrijf de tarball naar `stdout`:

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` -`

- Schrijf de tarball naar een bestand:

`crane export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>

- Lees de image vanuit `stdin`:

`crane export - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/filenaam</span>
