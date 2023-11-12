---
layout: page
title: windows/choco-apikey (Deutsch)
description: "Verwalte die API-Schlüssel für die Quellen von Chocolatey."
content_hash: eac042b801536103df4375b415627f654e1e74f2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-apikey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-apikey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco apikey

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
