---
layout: page
title: common/npx (Deutsch)
description: "Führt Binärdateien von `npm` Paketen aus."
content_hash: bbb76a65504e71e3d21b0c948e38800d87ebde96
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/npx.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/npx.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# npx

Führt Binärdateien von `npm` Paketen aus.
Weitere Informationen: <https://github.com/npm/npx>.

- Führe die Binärdatei eines bestimmten npm Pakets aus:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehlsargumente</span>

- Übergib den konkreten Namen, falls das Paket mehrere Binärdateien besitzt:

`npx --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulname</span>

- Führe einen Befehl aus, wenn er im aktuellen Verzeichnis oder in `node_modules/.bin` gefunden wird:

`npx --no-install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehlsargumente</span>

- Führe die Binärdatei eines bestimmten npm Moduls aus und unterdrücke jede Ausgabe von `npx` selbst:

`npx --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulname</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehlsargumente</span>

- Zeige eine Hilfe an:

`npx --help`
