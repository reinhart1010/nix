---
layout: page
title: common/lpstat (Nederlands)
description: "Bekijk de status informatie over printers."
content_hash: 4f93455401b302fadb2df2af7ae51d44ebb46acb
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/lpstat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/lpstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpstat

Bekijk de status informatie over printers.
Meer informatie: <https://manned.org/lpstat>.

- Toon alle printers op de machine en of deze ingeschakeld zijn om te printen:

`lpstat -p`

- Toon de standaard printer:

`lpstat -d`

- Toon alle beschikbare status informatie:

`lpstat -t`

- Toon een lijst van printtaken in de wachtrij voor een specifieke gebruiker:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>
