---
layout: page
title: common/plantuml (Deutsch)
description: "Erstelle UML-Diagramme aus einer reinen Textsprache und rendere sie in verschiedenen Formaten."
content_hash: 1ae0d2815b17cbfa381efb47e540470dc13fb0ea
related_topics:
  - title: English version
    url: /en/common/plantuml.html
    icon: bi bi-globe
---
# plantuml

Erstelle UML-Diagramme aus einer reinen Textsprache und rendere sie in verschiedenen Formaten.
Weitere Informationen: <https://plantuml.com/en/command-line>.

- Rendere Diagramme im Standardformat (PNG):

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm1.puml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm2.puml</span>

- Rendere eine Diagramm im vorgegebenen Format (z.B. `png`, `pdf`, `svg`, `txt`):

`plantuml -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm.puml</span>

- Rendere alle Diagramme eines Verzeichnisses:

`plantuml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>

- Rendere ein Diagramm in ein bestimmtes Ausgabeverzeichnis:

`plantuml -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/verzeichnis</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm.puml</span>

- Rendere ein Diagramm mit einer bestimmten Konfigurationsdatei:

`plantuml -config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/konfig.cfg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/diagramm.puml</span>

- Zeige Hilfe an:

`plantuml -help`
