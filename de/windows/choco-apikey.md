---
layout: page
title: windows/choco-apikey (Deutsch)
description: "Verwalte die API-Schlüssel für die Quellen von Chocolatey."
content_hash: 645fd3053d67ac087a20aa61418e285cc0217f90
related_topics:
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
---
# choco-apikey

Verwalte die API-Schlüssel für die Quellen von Chocolatey.
Weitere Informationen: <https://chocolatey.org/docs/commands-apikey>.

- Gib eine Liste von Quellen und ihren API-Schlüsseln aus:

`choco apikey`

- Zeige eine bestimmte Quelle und ihren API-Schlüssel an:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quell_url</span>`"`

- Setze den API-Schlüssel für eine Quelle:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quell_url</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_schluessel</span>`"`

- Entferne den API-Schlüssel einer Quelle:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quell_url</span>`" --remove`
