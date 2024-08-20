---
layout: page
title: osx/lpstat (Nederlands)
description: "Toon statusinformatie over de huidige klassen, printopdrachten en printers."
content_hash: 8f532d87410effafb0be0b36e5001aff7c08d865
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/osx/lpstat.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/lpstat.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lpstat

Toon statusinformatie over de huidige klassen, printopdrachten en printers.
Meer informatie: <https://keith.github.io/xcode-man-pages/lpstat.1.html>.

- Toon een lange lijst van printers, klassen en printopdrachten:

`lpstat -l`

- Forceer encryptie bij verbinding met de CUPS-server:

`lpstat -E`

- Toon de ranglijst van printopdrachten:

`lpstat -R`

- Toon of de CUPS-server wel of niet draait:

`lpstat -r`

- Toon alle statusinformatie:

`lpstat -t`
