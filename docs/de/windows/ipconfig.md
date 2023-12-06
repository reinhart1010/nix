---
layout: page
title: windows/ipconfig (Deutsch)
description: "Zeige die Netzwerkkonfiguration von Windows an und verwalte diese."
content_hash: 4b536b79ffbb9ed3c8d8911de6a9d08b0b7a286d
last_modified_at: 2023-12-06
related_topics:
  - title: English version
    url: /en/windows/ipconfig.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/ipconfig.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ipconfig

Zeige die Netzwerkkonfiguration von Windows an und verwalte diese.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Zeige eine Liste der Netzwerkadapter an:

`ipconfig`

- Zeige eine detaillierte Liste der Netzwerkadapter an:

`ipconfig /all`

- Erneuere die IP-Adressen für einen Netzwerkadapter:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Adapter</span>

- Gib die IP-Adressen für einen Netzwerkadapter frei:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Adapter</span>

- Zeige den lokalen DNS-Cache an:

`ipconfig /displaydns`

- Entferne alle Einträge aus dem lokalen DNS-Cache:

`ipconfig /flushdns`
