---
layout: page
title: common/pip (Deutsch)
description: "Python package manager."
content_hash: de22cb2f227df869382ebb256b98cfcde0a19f1d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pip

Python package manager.
Einige Unterbefehle wie `pip install` sind separat dokumentiert.
Weitere Informationen: <https://pip.pypa.io>.

- Installiere ein Paket (siehe `pip install` für weitere Beispiele):

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Installiere ein Paket im Benutzerverzeichnis, anstatt systemweit:

`pip install --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Aktualisiere ein Paket:

`pip install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Deinstalliere ein Paket:

`pip uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Speichere eine Liste aller installierten Pakete in eine Datei:

`pip freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- Zeige Informationen über ein installiertes Paket an:

`pip show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>

- Installiere Pakete, die in einer Datei gelistet sind:

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>
