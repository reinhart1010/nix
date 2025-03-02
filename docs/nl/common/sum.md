---
layout: page
title: common/sum (Nederlands)
description: "Bereken checksums en het aantal blokken voor een bestand."
content_hash: 050283a759af187ced45221dfe35b7d2e79cae5e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sum

Bereken checksums en het aantal blokken voor een bestand.
Een voorloper van de modernere `cksum`.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sum-invocation.html>.

- Bereken een checksum met een BSD-compatibel algoritme en 1024-byte blokken:

`sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Bereken een checksum met een System V-compatibel algoritme en 512-byte blokken:

`sum --sysv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
