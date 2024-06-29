---
layout: page
title: common/sum (Nederlands)
description: "Bereken checksums en het aantal blokken voor een bestand."
content_hash: 79cec3cbf30e739d3b1d0f9360012a6265172deb
last_modified_at: 2024-06-29
related_topics:
  - title: English version
    url: /en/common/sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sum

Bereken checksums en het aantal blokken voor een bestand.
Een voorloper van de modernere `cksum`.
Meer informatie: <https://www.gnu.org/software/coreutils/sum>.

- Bereken een checksum met een BSD-compatibel algoritme en 1024-byte blokken:

`sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Bereken een checksum met een System V-compatibel algoritme en 512-byte blokken:

`sum --sysv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
