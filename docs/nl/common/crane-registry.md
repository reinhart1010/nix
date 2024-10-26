---
layout: page
title: common/crane-registry (Nederlands)
description: "Dit commando biedt een registry-implementatie op een automatisch gekozen poort (:0), $PORT of --address."
content_hash: d89c3d3bfe498334f9e99846267e0545b19739fb
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-registry.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-registry.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-registry.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane registry

Dit commando biedt een registry-implementatie op een automatisch gekozen poort (:0), $PORT of --address.
Het commando blokkeert terwijl de server pushes en pulls accepteert en de inhoud kan worden opgeslagen in het geheugen en op de schijf.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>.

- Dien een registry-implementatie:

`crane registry serve`

- Adres om naar te luisteren:

`crane registry serve --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_naam</span>

- Pad naar een directory waar blobs worden opgeslagen:

`crane registry serve --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/store_dir</span>

- Toon help voor `crane registry`:

`crane registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>

- Toon help voor `crane registry serve`:

`crane registry serve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
