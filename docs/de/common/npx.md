---
layout: page
title: common/npx (Deutsch)
description: "Führt Binärdateien von `npm` Paketen aus."
content_hash: bbb76a65504e71e3d21b0c948e38800d87ebde96
related_topics:
  - title: English version
    url: /en/common/npx.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npx

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
