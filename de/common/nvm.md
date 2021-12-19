---
layout: page
title: common/nvm (Deutsch)
description: "Installiere, deinstalliere oder wechsle zwischen Node.js Versionen."
content_hash: 753298e16bb81e7168db7f20042b7f904f49f822
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
Unterstützt Versionsnummern wie "0.12" oder "v4.2", und Label wie "stable", "system", etc.
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
