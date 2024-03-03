---
layout: page
title: common/duf (Deutsch)
description: "Festplattennutzung/freie Verwendbarkeit."
content_hash: c9cfcdb57e4355253b4dad79452d3d5dfdedd779
last_modified_at: 2024-03-03
related_topics:
  - title: English version
    url: /en/common/duf.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># duf

Festplattennutzung/freie Verwendbarkeit.
Weitere Informationen: <https://github.com/muesli/duf>.

- Liste zugängliche Geräte auf:

`duf`

- Liste alles auf (auch pseudo-, doppelte oder unzugängliche Dateisysteme):

`duf --all`

- Zeige nur konkrete Geräte oder Mountpoints:

`duf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis1 pfad/zu/verzeichnis2 ...</span>

- Sortiere die Ergebnisse nach einem spezifischen Kriterium:

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size|used|avail|usage</span>
