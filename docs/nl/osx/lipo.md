---
layout: page
title: osx/lipo (Nederlands)
description: "Tool voor het verwerken van Mach-O Universal Binaries."
content_hash: 1a29596b9440d9ecd3b994946d66757166630dd9
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/lipo.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/lipo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lipo

Tool voor het verwerken van Mach-O Universal Binaries.
Meer informatie: <https://keith.github.io/xcode-man-pages/lipo.1.html>.

- Maak een universeel bestand uit twee bestanden met één architectuur:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand.x86_64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand.arm64e</span>` -create -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>

- Toon alle architecturen die een universeel bestand bevat:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>` -archs`

- Toon gedetailleerde informatie over een universeel bestand:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>` -detailed_info`

- Pak een bestand met één architectuur uit uit een universeel bestand:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>` -thin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64e</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand.arm64e</span>
