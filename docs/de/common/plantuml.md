---
layout: page
title: common/plantuml (Deutsch)
description: "Erstelle UML-Diagramme aus einer reinen Textsprache und rendere sie in verschiedenen Formaten."
content_hash: 608c3e683f14635af549bf50a99ac42f742c05f4
last_modified_at: 2024-05-11
related_topics:
  - title: English version
    url: /en/common/plantuml.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># plantuml

Erstelle UML-Diagramme aus einer reinen Textsprache und rendere sie in verschiedenen Formaten.
Weitere Informationen: <https://plantuml.com/en/command-line>.

- Rendere Diagramme im Standardformat (PNG):

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm1.puml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm2.puml</span>

- Rendere ein Diagramm im vorgegebenen Format (z.B. `png`, `pdf`, `svg`, `txt`):

`plantuml -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm.puml</span>

- Rendere alle Diagramme eines Verzeichnisses:

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Rendere ein Diagramm in ein bestimmtes Ausgabeverzeichnis:

`plantuml -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm.puml</span>

- Rendere ein Diagramm mit einer bestimmten Konfigurationsdatei:

`plantuml -config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/konfig.cfg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm.puml</span>

- Zeige Hilfe an:

`plantuml -help`
