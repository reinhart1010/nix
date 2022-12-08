---
layout: page
title: common/lpinfo (Deutsch)
description: "Liste verbundene Drucker und installierte Treiber für den CUPS Druckserver."
content_hash: a7359e7411781f6797b64b61ee4042f048427713
last_modified_at: 2022-12-08
related_topics:
  - title: English version
    url: /en/common/lpinfo.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lpinfo

Liste verbundene Drucker und installierte Treiber für den CUPS Druckserver.
Weitere Informationen: <https://www.cups.org/doc/man-lpinfo.html>.

- Liste alle aktuell verbundenen Drucker auf:

`lpinfo -v`

- Liste alle aktuell installierten Druckertreiber auf:

`lpinfo -m`

- Suche installierte Druckertreiber nach Hersteller oder Modell:

`lpinfo --make-and-model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">druckermodell</span>`" -m`
