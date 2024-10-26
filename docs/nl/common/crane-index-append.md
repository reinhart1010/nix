---
layout: page
title: common/crane-index-append (Nederlands)
description: "Voeg een manifest toe aan een remote index."
content_hash: 7fa1699af76aa2180a6aed2ca37f8d6751ed3e36
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/common/crane-index-append.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-index-append.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crane-index-append.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crane index append

Voeg een manifest toe aan een remote index.
Dit subcommando pusht een index op basis van een (optionele) basisindex, met toegevoegde manifests.
Het platform voor toegevoegde manifests wordt afgeleid van het configuratiebestand of weggelaten als dat niet haalbaar is.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>.

- Voeg een manifest toe aan een remote index:

`crane index append`

- Verwijs naar manifests om toe te voegen aan de basisindex:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--manifest</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manifest_naam1 manifest_naam2 ...</span>

- Tag die toegepast moet worden op de resulterende image:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Lege basisindex heeft Docker-media types in plaats van OCI:

`crane index append --docker-empty-base`

- Voeg elk van zijn kinderen toe in plaats van de index zelf (standaard waar):

`crane index append --flatten`

- Toon help:

`crane index append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
