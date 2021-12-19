---
layout: page
title: common/nodenv (Deutsch)
description: "Ein Tool, um Node.js Versionen zu verwalten."
content_hash: ed4d3805d222cf9845433c2df1f74c4d8aaf38a8
related_topics:
  - title: English version
    url: /en/common/nodenv.html
    icon: bi bi-globe
---
# nodenv

Ein Tool, um Node.js Versionen zu verwalten.
Weitere Informationen: <https://github.com/nodenv/nodenv>.

- Installiere eine bestimmte Node.js Version:

`nodenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Zeige eine Liste von verfügbaren Versionen:

`nodenv install --list`

- Verwende systemweit eine bestimmte Node.js Version:

`nodenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Verwende eine bestimmte Node.js Version im aktuellen Verzeichnis:

`nodenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version</span>

- Zeige die verwendete Node.js Version im aktuellen Verzeichnis:

`nodenv version`

- Zeige den Ort, wo ein Node.js Befehl installiert ist (bspw. `npm`):

`nodenv which `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>
