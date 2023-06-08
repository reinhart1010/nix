---
layout: page
title: common/agate (Nederlands)
description: "Een eenvoudige server voor het Gemini-netwerkprotocol."
content_hash: 57e27d42c7a05b0307fcbd5fba692e947798f97a
last_modified_at: 2023-06-08
related_topics:
  - title: English version
    url: /en/common/agate.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/agate.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/agate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/agate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/agate.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># agate

Een eenvoudige server voor het Gemini-netwerkprotocol.
Meer informatie: <https://github.com/mbrubeck/agate>.

- Voer een persoonlijke sleutel en certificaat uit en genereer deze:

`agate --content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/inhoud/</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[::]:1965</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0:1965</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.com</span>` --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nl-NL</span>

- Server starten:

`agate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Help weergeven:

`agate -h`
