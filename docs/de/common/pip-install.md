---
layout: page
title: common/pip-install (Deutsch)
description: "Installiere Python-Pakete."
content_hash: 29ec1fc5e5ce595abbc172c07634c46ce8249d0f
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/pip-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pip-install.html
    icon: bi bi-globe
tldri18n_status: 2
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

`pip install --find-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|pfad/zu/datei</span>

- Installiere das lokale Paket im aktuellen Verzeichnis im Entwicklungs-/Bearbeitungsmodus:

`pip install --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>
