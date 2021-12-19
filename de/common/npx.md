---
layout: page
title: common/npx (Deutsch)
description: "Führt Binärdateien von `npm` Paketen aus."
content_hash: 19c418a75b25108b73fa7d85e6ac1707df7feeec
related_topics:
  - title: English version
    url: /en/common/npx.html
    icon: bi bi-globe
---
# npx

Führt Binärdateien von `npm` Paketen aus.
Weitere Informationen: <https://www.npmjs.com/package/npx>.

- Führe die Binärdatei eines übergebenen npm Pakets aus:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Übergib den konkreten Namen, falls das Paket mehrere Binärdateien besitzt:

`npx -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Zeige eine Hilfe an:

`npx --help`
