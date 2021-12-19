---
layout: page
title: common/npm (Deutsch)
description: "Ein Kommandozeilenwerkzeug für die Verwaltung von JavaScript und Node.js Paketen (Packages)."
content_hash: 163b21587b320d1aaeba9ed8bf3523c9219d3ffd
related_topics:
  - title: English version
    url: /en/common/npm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/npm.html
    icon: bi bi-globe
---
# npm

Ein Kommandozeilenwerkzeug für die Verwaltung von JavaScript und Node.js Paketen (Packages).
Weitere Informationen: <https://www.npmjs.com/>.

- Erstelle eine `package.json` Datei interaktiv:

`npm init`

- Installiere alle in der `package.json` Datei gelisteten Abhängigkeiten:

`npm install`

- Installiere eine spezifische Version eines Packages und füge es automatisch der `package.json` Datei hinzu:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Installiere ein Package und füge es als Entwicklungs-Abhängigkeit der `package.json` Datei hinzu:

`npm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>` --save-dev`

- Installiere ein Package global:

`npm install --global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Deinstalliere ein Package und entferne es automatisch aus der `package.json` Datei:

`npm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Gib eine Liste aller lokal installierten Packages aus:

`npm list`

- Gib eine Liste aller global installierten Packages aus:

`npm list --global --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
