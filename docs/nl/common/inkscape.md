---
layout: page
title: common/inkscape (Nederlands)
description: "Een SVG (Scalable Vector Graphics) bewerkingsprogramma."
content_hash: 9627d8680a29836f2c0c017c25661825ac163b1c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/inkscape.html
    icon: bi bi-globe
tldri18n_status: 2
---
# inkscape

Een SVG (Scalable Vector Graphics) bewerkingsprogramma.
Voor Inkscape versies tot en met 0.92.x, gebruik -e in plaats van -o.
Meer informatie: <https://inkscape.org>.

- Open een SVG-bestand in de Inkscape GUI:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.svg</span>

- Exporteer een SVG-bestand in een bitmap met het standaardformaat (PNG) en de standaardresolutie (96 DPI):

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.png</span>

- Exporteer een SVG-bestand in een bitmap van 600x400 pixels (vervorming van de aspectverhouding mogelijk):

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.png</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>

- Exporteer de tekening (selectiekader van alle objecten) van een SVG-bestand in een bitmap:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.png</span>` -D`

- Exporteer een enkel object, gezien zijn ID, in een bitmap:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.svg</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">object.png</span>

- Exporteer een SVG-document naar PDF, converteer alle teksten naar paden:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.svg</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.pdf</span>` --export-text-to-path`

- Dupliceer het object met id="pad123", roteer het duplicaat 90 graden, sla het bestand op, en sluit Inkscape af:

`inkscape `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam.svg</span>` --select=path123 --verb="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EditDuplicate;ObjectRotate90;FileSave;FileQuit</span>`"`
