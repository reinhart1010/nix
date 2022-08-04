---
layout: page
title: common/npx (Deutsch)
description: "Führt Binärdateien von `npm` Paketen aus."
content_hash: 0498e0cfaa67de73a8aaacf0098b6ba2cd23448d
related_topics:
  - title: English version
    url: /en/common/npx.html
    icon: bi bi-globe
---
# npx

Führt Binärdateien von `npm` Paketen aus.
Weitere Informationen: <https://github.com/npm/npx>.

- Führe die Binärdatei eines übergebenen npm Pakets aus:

`npx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Übergib den konkreten Namen, falls das Paket mehrere Binärdateien besitzt:

`npx -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modul_name</span>

- Zeige eine Hilfe an:

`npx --help`
