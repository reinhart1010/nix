---
layout: page
title: osx/lipo (Nederlands)
description: "Tool voor het verwerken van Mach-O Universal Binaries."
content_hash: 634f4ad465b43e491c08798bf2f79b8a81dc0d55
last_modified_at: 2023-11-17
related_topics:
  - title: English version
    url: /en/osx/lipo.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/lipo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/lipo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lipo

Tool voor het verwerken van Mach-O Universal Binaries.
Meer informatie: <https://ss64.com/osx/lipo.html>.

- Maak een universeel bestand uit twee bestanden met één architectuur:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand.x86_64</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand.arm64e</span>` -create -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>

- Toon alle architecturen die een universeel bestand bevat:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>` -archs`

- Toon gedetailleerde informatie over een universeel bestand:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>` -detailed_info`

- Pak een bestand met één architectuur uit uit een universeel bestand:

`lipo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand</span>` -thin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arm64e</span>` -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/binary_bestand.arm64e</span>
