---
layout: page
title: common/nvm (Nederlands)
description: "Installeer, deïnstalleer of wissel tussen verschillende Node.js-versies."
content_hash: 0965c6b3e1dcfb0796c18d7170b54e2bde0ffaf6
last_modified_at: 2025-01-03
related_topics:
  - title: Deutsch version
    url: /de/common/nvm.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nvm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvm

Installeer, deïnstalleer of wissel tussen verschillende Node.js-versies.
Ondersteunt versienummers zoals "12.8" of "v16.13.1", en labels zoals "stable", "system", enz.
Bekijk ook: `asdf`.
Meer informatie: <https://github.com/creationix/nvm>.

- Installeer een specifieke versie van Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Gebruik een specifieke versie van Node.js in de huidige shell:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Stel de standaardversie van Node.js in:

`nvm alias default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Toon alle beschikbare Node.js-versies en markeer de standaardversie:

`nvm list`

- Deïnstalleer een bepaalde versie van Node.js:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>

- Start de REPL van een specifieke versie van Node.js:

`nvm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>` --version`

- Voer een script uit in een specifieke versie van Node.js:

`nvm exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_versie</span>` node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>
