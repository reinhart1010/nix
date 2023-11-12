---
layout: page
title: common/pnpm (Deutsch)
description: "Schneller, speicherplatzsparender Paketmanager für Node.js."
content_hash: 484de277ffa8e5c1c869cb7ca03c29c533ab346d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pnpm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pnpm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pnpm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pnpm

Schneller, speicherplatzsparender Paketmanager für Node.js.
Ein Kommandozeilenwerkzeug für die Verwaltung von JavaScript und Node.js Paketen (Packages).
Weitere Informationen: <https://pnpm.io>.

- Erstelle eine `package.json` Datei interaktiv:

`pnpm init`

- Installiere alle in der `package.json` Datei gelisteten Abhängigkeiten:

`pnpm install`

- Installiere eine spezifische Version eines Packages und füge es automatisch der `package.json` Datei hinzu:

`pnpm add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Installiere ein Package und füge es als Entwicklungs-Abhängigkeit der `package.json` Datei hinzu:

`pnpm add -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Installiere ein Package global:

`pnpm add -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Deinstalliere ein Package und entferne es automatisch aus der `package.json` Datei:

`pnpm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Gib eine Liste aller lokal installierten Packages aus:

`pnpm list`

- Gib eine Liste aller global installierten Packages aus:

`pnpm list -g --depth=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>
