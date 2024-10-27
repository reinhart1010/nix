---
layout: page
title: common/crane-copy (Nederlands)
description: "Kopieer efficiënt een remote image van bron naar doel terwijl de digest-waarde behouden blijft."
content_hash: 077901daa4107f281401743d52afe222f3af525d
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/crane-copy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane copy

Kopieer efficiënt een remote image van bron naar doel terwijl de digest-waarde behouden blijft.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_copy.md>.

- Kopieer een image van bron naar doel:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>

- Kopieer alle tags:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--all-tags</span>

- Stel het maximum aantal gelijktijdige kopieën in, standaard is GOMAXPROCS:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--jobs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">int</span>

- Voorkom het overschrijven van bestaande tags in het doel:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doel</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--no-clobber</span>

- Toon help:

`crane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
