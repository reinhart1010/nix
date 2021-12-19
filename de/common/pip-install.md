---
layout: page
title: common/pip-install (Deutsch)
description: "Installiere Python-Pakete."
content_hash: b5046ff9552b10989c48a8661f7ee0628287ba1e
related_topics:
  - title: English version
    url: /en/common/pip-install.html
    icon: bi bi-globe
---
# pip install

Installiere Python-Pakete.
Weitere Informationen: <https://pip.pypa.io>.

- Installiere ein Paket:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Installiere eine spezifische Paketversion:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketversion</span>

- Installiere die Pakete aus einer Datei:

`pip install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Installiere die Pakete von einer URL oder einem lokalen Archiv (.tar.gz | .whl):

`pip install -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|pfad/zur/datei</span>

- Installiere das lokale Paket im aktuellen Verzeichnis im Entwicklungs-/Bearbeitungsmodus:

`pip install -e .`
