---
layout: page
title: common/pdfseparate (Deutsch)
description: "Extrahiere die Seiten einer Portable Document Format (PDF) Datei."
content_hash: d88bf1bc157f0d1a8227e3afdd83f733a0a17b5d
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/common/pdfseparate.html
    icon: bi bi-globe
---
# pdfseparate

Extrahiere die Seiten einer Portable Document Format (PDF) Datei.
Weitere Informationen: <https://manpages.debian.org/latest/poppler-utils/pdfseparate.1.en.html>.

- Extrahiere die Seiten einer PDF Datei und speichere jede Seite als neue PDF Datei ab:

`pdfseparate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zieldatei-%d.pdf</span>

- Gib die erste Seite zum Extrahieren an:

`pdfseparate -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zieldatei-%d.pdf</span>

- Gib die letzte Seite zum Extrahieren an:

`pdfseparate -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/quelldatei.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/zieldatei-%d.pdf</span>
