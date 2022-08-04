---
layout: page
title: common/nvm (Deutsch)
description: "Installiere, deinstalliere oder wechsle zwischen Node.js Versionen."
content_hash: f7535bb8f75a1e27539584fc5dfe4ebff9ae3adf
related_topics:
  - title: English version
    url: /en/common/nvm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvm.html
    icon: bi bi-globe
---
# nvm

Installiere, deinstalliere oder wechsle zwischen Node.js Versionen.
Unterstützt Versionsnummern wie "12.8" oder "v16.13.1", und Label wie "stable", "system", etc.
Weitere Informationen: <https://github.com/creationix/nvm>.

- Installiere eine bestimmte Node.js Version:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Verwende eine bestimmte Node.js Version in der aktuellen Shell:

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Setze die Node.js-Standardversion:

`nvm alias default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Zeige alle verfügbaren Node.js Versionen und hebe die Standardversion hervor:

`nvm list`

- Deinstalliere die angegebene Node.js Version:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>

- Starte eine REPL mit einer bestimmten Node.js Version:

`nvm run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>` --version`

- Führe ein Skript mit einer bestimmten Node.js Version aus:

`nvm exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node_version</span>` node `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>
