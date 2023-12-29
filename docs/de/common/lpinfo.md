---
layout: page
title: common/lpinfo (Deutsch)
description: "Liste verbundene Drucker und installierte Treiber für den CUPS Druckserver."
content_hash: 2c8310ba0ae0afce14d7aa8f9933c05b1d208034
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/lpinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpinfo

Liste verbundene Drucker und installierte Treiber für den CUPS Druckserver.
Weitere Informationen: <https://openprinting.github.io/cups/doc/man-lpinfo.html>.

- Liste alle aktuell verbundenen Drucker auf:

`lpinfo -v`

- Liste alle aktuell installierten Druckertreiber auf:

`lpinfo -m`

- Suche installierte Druckertreiber nach Hersteller oder Modell:

`lpinfo --make-and-model "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">druckermodell</span>`" -m`
