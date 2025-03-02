---
layout: page
title: common/gcrane-copy (Nederlands)
description: "Kopieer efficiënt een afbeelding van de ene locatie naar de andere terwijl de digestwaarde behouden blijft."
content_hash: d1a66ca3f44672464c594aa0d5e94b2780a43ccc
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/gcrane-copy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcrane-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane copy

Kopieer efficiënt een afbeelding van de ene locatie naar de andere terwijl de digestwaarde behouden blijft.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Kopieer een afbeelding van bron naar doel:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cp|copy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>

- Stel het maximale aantal gelijktijdige kopieën in, standaard is 20:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--jobs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal_kopieën</span>

- Of de repositories doorzocht moeten worden:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Toon de help:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
