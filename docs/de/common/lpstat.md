---
layout: page
title: common/lpstat (Deutsch)
description: "Zeige Statusinformationen von Druckern."
content_hash: b44323b1ccac78f57628b90e9262c72e96b6a789
last_modified_at: 2022-12-08
related_topics:
  - title: English version
    url: /en/common/lpstat.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># lpstat

Zeige Statusinformationen von Druckern.
Weitere Informationen: <https://manned.org/lpstat>.

- Liste alle aktuell verbundenen Drucker mit ihrer Druckverfügbarkeit auf:

`lpstat -p`

- Zeige den Standarddrucker an:

`lpstat -d`

- Zeige alle Statusinformationen an:

`lpstat -t`

- Liste alle Druckaufträge von einem gegebenen Nutzer auf:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nutzer</span>
