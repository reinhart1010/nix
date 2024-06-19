---
layout: page
title: osx/wc (Nederlands)
description: "Tel regels, woorden of bytes."
content_hash: 126a3d7a99397e0b63cb3ae8562d3038435bc83d
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/wc.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Tel regels, woorden of bytes.
Meer informatie: <https://keith.github.io/xcode-man-pages/wc.1.html>.

- Tel regels in een bestand:

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Tel woorden in een bestand:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Tel tekens (bytes) in een bestand:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Tel tekens in een bestand (rekening houdend met multi-byte tekensets):

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Gebruik `stdin` om regels, woorden en tekens (bytes) in die volgorde te tellen:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
